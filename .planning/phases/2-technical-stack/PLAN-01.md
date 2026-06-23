# Phase 2: Technical Stack

## Phase Goal
Select and justify the technology stack, frameworks, and tools.

## Tech Stack
Python, Django, Amazon Web Services, RESTful API, API, PostgreSQL

## Files to Create

```file:requirements.txt
Django>=5.0
djangorestframework>=3.14
psycopg2-binary
gunicorn
celery>=5.3
redis
boto3
python-dotenv
pytest>=8.0

```

```file:.env.example
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dbname
SECRET_KEY=***replace-with-random-secret***
```

```file:Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true
COPY . .
EXPOSE 8000
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

```file:docker-compose.yml
version: '3.9'
services:
  api:
    build: .
    ports: ['8000:8000']
    env_file: .env
    depends_on:
      postgres:
        condition: service_healthy
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppassword
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U appuser']
      interval: 5s
      timeout: 5s
      retries: 5
volumes:
  pgdata:
```

## Done When
- requirements.txt lists all dependencies
- .env.example documents all environment variables
- Dockerfile builds: docker build .
- docker-compose.yml starts all services: docker compose up
