# Senior Backend Developer — Django, AWS, Python

**Built by: KMan | AI-Augmented Engineering Factory**

## Business Problem Solved

This project replaces manual, error-prone backend infrastructure with a production-grade Django system that integrates AI agent capabilities. By building on Django REST Framework with LangGraph orchestration, it enables structured AI tool-calling, document processing pipelines, and LLM-powered retrieval — reducing operational overhead and accelerating development cycles for teams relying on AWS-based backend services.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your DATABASE_URL, SECRET_KEY, AWS credentials

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Tech Stack

Python, Django 5, Django REST Framework, PostgreSQL, LangGraph, LangChain, AWS (boto3), Celery, Redis, Docker, Gunicorn, GitHub Actions

## Project Structure

```
.
├── api/                  # Django app with models, admin, REST views
├── config/               # Django project settings (settings.py, urls.py, wsgi.py)
├── migrations/           # Database migrations
├── tests/                # Test suite
├── Dockerfile            # Production container
├── docker-compose.yml    # Local development stack
├── manage.py             # Django management CLI
└── requirements.txt      # Python dependencies
```

## API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/health | Health check |
| POST | /api/v1/chat | Chat with AI agent |

## Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_URL | PostgreSQL connection string |
| SECRET_KEY | Django secret key |
| DEBUG | Enable debug mode |
| AWS_ACCESS_KEY_ID | AWS credentials |
| AWS_SECRET_ACCESS_KEY | AWS credentials |
| OPENAI_API_KEY | LLM API key |

## Docker

```bash
# Build and run
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate
```
