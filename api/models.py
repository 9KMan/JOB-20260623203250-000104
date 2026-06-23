"""Database models for the Django + AI agent backend.

The models defined here MUST stay in sync with
``api/migrations/0001_initial.py``. Field types, choices, indexes, and
constraints are derived directly from the initial migration so that
``python manage.py makemigrations`` produces no further changes.
"""
import uuid

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """Abstract base providing UUID primary key and audit timestamps."""

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        serialize=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Document(BaseModel):
    """A piece of content uploaded for indexing / RAG retrieval."""

    STATUS_PENDING = "pending"
    STATUS_PROCESSING = "processing"
    STATUS_INDEXED = "indexed"
    STATUS_FAILED = "failed"
    STATUS_ARCHIVED = "archived"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_INDEXED, "Indexed"),
        (STATUS_FAILED, "Failed"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    title = models.CharField(max_length=512)
    source = models.CharField(blank=True, max_length=1024)
    content_type = models.CharField(blank=True, max_length=128)
    content = models.TextField(blank=True)
    size_bytes = models.BigIntegerField(default=0)
    checksum = models.CharField(blank=True, max_length=128, db_index=True)
    status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        db_index=True,
    )
    error = models.TextField(blank=True)
    document_metadata = models.JSONField(blank=True, default=dict)
    indexed_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["status", "-created_at"]),
            models.Index(fields=["content_type", "status"]),
        ]

    def __str__(self) -> str:
        return self.title


class Conversation(BaseModel):
    """A user-facing chat / agent conversation."""

    title = models.CharField(blank=True, max_length=255)
    agent_name = models.CharField(blank=True, max_length=128)
    conversation_metadata = models.JSONField(blank=True, default=dict)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversations",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-updated_at",)
        indexes = [
            models.Index(fields=["user", "-updated_at"]),
            models.Index(fields=["agent_name", "-updated_at"]),
        ]

    def __str__(self) -> str:
        return self.title or f"Conversation {self.id}"


class Message(BaseModel):
    """A single message inside a :class:`Conversation`."""

    ROLE_SYSTEM = "system"
    ROLE_USER = "user"
    ROLE_ASSISTANT = "assistant"
    ROLE_TOOL = "tool"
    ROLE_CHOICES = [
        (ROLE_SYSTEM, "System"),
        (ROLE_USER, "User"),
        (ROLE_ASSISTANT, "Assistant"),
        (ROLE_TOOL, "Tool"),
    ]

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="replies",
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=16,
        choices=ROLE_CHOICES,
        db_index=True,
    )
    content = models.TextField(blank=True)
    name = models.CharField(blank=True, max_length=128)
    tool_calls = models.JSONField(blank=True, default=list)
    tool_call_id = models.CharField(blank=True, max_length=128)
    message_metadata = models.JSONField(blank=True, default=dict)

    class Meta:
        ordering = ("conversation", "created_at")
        indexes = [
            models.Index(fields=["conversation", "created_at"]),
            models.Index(fields=["role", "created_at"]),
        ]

    def __str__(self) -> str:
        preview = (self.content or "").splitlines()[0] if self.content else ""
        return f"[{self.role}] {preview[:80]}"


class AgentTool(BaseModel):
    """A tool the agent can invoke during orchestration."""

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    handler = models.CharField(max_length=255)
    schema = models.JSONField(blank=True, default=dict)
    config = models.JSONField(blank=True, default=dict)
    is_enabled = models.BooleanField(db_index=True, default=True)
    timeout_seconds = models.PositiveIntegerField(default=30)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class DocumentChunk(BaseModel):
    """A chunked slice of a :class:`Document` ready for embedding."""

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="chunks",
    )
    ordinal = models.PositiveIntegerField()
    content = models.TextField()
    token_count = models.PositiveIntegerField(default=0)
    vector_id = models.CharField(blank=True, max_length=256, db_index=True)
    chunk_metadata = models.JSONField(blank=True, default=dict)

    class Meta:
        ordering = ("document", "ordinal")
        indexes = [
            models.Index(fields=["document", "ordinal"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=("document", "ordinal"),
                name="documentchunk_document_ordinal_unique",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.document_id}:{self.ordinal}"


class LambdaFunction(BaseModel):
    """A tracked AWS Lambda invocation."""

    STATUS_PENDING = "pending"
    STATUS_RUNNING = "running"
    STATUS_SUCCEEDED = "succeeded"
    STATUS_FAILED = "failed"
    STATUS_TIMED_OUT = "timed_out"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_RUNNING, "Running"),
        (STATUS_SUCCEEDED, "Succeeded"),
        (STATUS_FAILED, "Failed"),
        (STATUS_TIMED_OUT, "Timed Out"),
    ]

    name = models.CharField(max_length=255, db_index=True)
    arn = models.CharField(blank=True, max_length=512)
    region = models.CharField(blank=True, max_length=64)
    payload = models.JSONField(blank=True, default=dict)
    response = models.JSONField(blank=True, default=dict)
    status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        db_index=True,
    )
    duration_ms = models.PositiveIntegerField(default=0)
    error = models.TextField(blank=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["name", "-created_at"]),
            models.Index(fields=["status", "-created_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.status})"