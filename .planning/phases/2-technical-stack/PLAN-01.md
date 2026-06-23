# Phase 02: Technical Stack

## Phase Goal
Select and justify the technology stack, frameworks, and tools for the Django Backend API.

## Tech Stack
- **Runtime:** Python 3.11
- **Framework:** Django 5 + Django REST Framework
- **Database:** PostgreSQL 15 (RDS)
- **AI Integration:** LangChain / LangGraph for agent orchestration
- **Cloud:** AWS (EC2, RDS, Route 53, IAM, Lambda, ECS)
- **Container:** Docker + docker-compose
- **Web Server:** Gunicorn + Nginx
- **Auth:** JWT (djangorestframework-simplejwt)
- **CI/CD:** GitHub Actions

## Dependencies
```
Django>=5.0
djangorestframework>=3.14
psycopg2-binary
gunicorn
celery
redis
boto3
langchain>=0.3
langgraph
pydantic
python-dotenv
gitleaks
```

## Environment Config
| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `AWS_ACCESS_KEY_ID` | AWS credentials |
| `AWS_SECRET_ACCESS_KEY` | AWS credentials |
| `SECRET_KEY` | Django secret key |
| `OPENAI_API_KEY` | LLM API key |
| `REDIS_URL` | Celery broker |

## Done When
- All dependencies documented in requirements.txt
- Docker setup complete and working
- AWS configuration documented
