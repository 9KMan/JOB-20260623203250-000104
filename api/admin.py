"""Django admin configuration for the API app."""
from django.contrib import admin

from .models import (
    AgentTool,
    Conversation,
    Document,
    DocumentChunk,
    LambdaFunction,
    Message,
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "size_bytes", "created_at", "indexed_at")
    list_filter = ("status", "content_type", "created_at")
    search_fields = ("title", "source", "content")
    readonly_fields = ("id", "created_at", "updated_at", "indexed_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title", "id", "user__username")
    readonly_fields = ("id", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "conversation", "role", "created_at")
    list_filter = ("role", "created_at")
    search_fields = ("content", "conversation__title")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("conversation", "created_at")


@admin.register(AgentTool)
class AgentToolAdmin(admin.ModelAdmin):
    list_display = ("name", "is_enabled", "created_at", "updated_at")
    list_filter = ("is_enabled",)
    search_fields = ("name", "description", "handler")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ("document", "ordinal", "token_count", "vector_id")
    list_filter = ("document",)
    search_fields = ("document__title", "content")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("document", "ordinal")


@admin.register(LambdaFunction)
class LambdaFunctionAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "region", "duration_ms", "created_at")
    list_filter = ("status", "region", "created_at")
    search_fields = ("name", "arn")
    readonly_fields = ("id", "created_at", "updated_at")
    date_hierarchy = "created_at"
