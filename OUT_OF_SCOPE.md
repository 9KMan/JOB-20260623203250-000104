# Out of Scope

The following items are explicitly **NOT** included in this build:

## Explicitly Excluded

- **Frontend UI** — This is a backend API only. No React/Vue/HTML templates.
- **User authentication** — No login, registration, or session management beyond basic JWT support.
- **Real-time WebSockets** — WebSocket support is noted in architecture but not implemented.
- **CI/CD pipeline** — GitHub Actions workflow is stubbed only.
- **Production AWS infrastructure** — No Terraform/CloudFormation; local Docker only.
- **AI agent tools** — LangGraph agent defined but specific tools (file ops, web search, etc.) deferred.
- **RAG pipeline** — Document ingestion and embedding pipeline deferred to later phase.
- **Email/SMS notifications** — No notification system.
- **Payment integration** — No Stripe or payment processing.
- **Multi-tenancy** — Single-tenant only.

## Future Phases

These items could be addressed in future iterations:

- **Frontend dashboard** — React admin panel for API monitoring
- **AI agent tool expansion** — File operations, web search, code execution
- **RAG implementation** — Document embedding and vector search
- **WebSocket support** — Real-time agent chat
- **Production AWS** — ECS, RDS, Lambda full deployment
- **Notification system** — Email/SMS alerts
- **CI/CD completion** — Full GitHub Actions pipeline with tests
