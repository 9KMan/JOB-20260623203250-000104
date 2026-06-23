# Senior Backend Developer — Django, AWS, Python

## 1. Overview

Build a production-grade Django backend system with AI agent capabilities.

## 2. Technical Stack

- **Runtime:** Python 3.11
- **Framework:** Django 5 + Django REST Framework
- **Database:** PostgreSQL 15 (RDS)
- **AI Integration:** LangChain / LangGraph for agent orchestration
- **Cloud:** AWS (EC2, RDS, Route 53, IAM, Lambda, ECS)
- **Container:** Docker + docker-compose
- **Web Server:** Gunicorn + Nginx
- **Auth:** JWT (djangorestframework-simplejwt)
- **CI/CD:** GitHub Actions

## 3. Architecture

- Django REST Framework API
- AI agent with tool-calling and document processing
- LLM-powered retrieval systems
- WebSocket support for real-time features
- CI/CD pipeline with GitHub Actions

## 4. Features

- REST API endpoints for all core entities
- AI agent orchestration via LangGraph
- Document processing pipeline
- Structured output generation
- Retrieval-augmented generation (RAG)
- AWS Lambda integration for serverless functions
- Docker containerization

## 5. Acceptance Criteria

- Django app starts without errors
- All API endpoints respond correctly
- Docker build succeeds
- CI/CD pipeline passes
- AI agent responds to tool calls
- PostgreSQL connection works
