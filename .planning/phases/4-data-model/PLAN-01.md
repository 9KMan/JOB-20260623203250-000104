# Phase 4: Data Model

## Phase Goal
Define the data model, entities, relationships, and storage approach.

## Files to Create

```file:api/models.py
"""Database models."""
from django.db import models


# Create your models here
```

```file:api/admin.py
"""Django admin configuration."""
from django.contrib import admin
from .models import *

# admin.site.register(ModelName)
```

## Done When
- python manage.py makemigrations succeeds
- python manage.py migrate succeeds
