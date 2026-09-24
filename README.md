# Multi-Container Architecture (Docker & Docker Compose)

A production-grade template demonstrating secure, multi-tier container orchestration using Docker, Docker Compose, Nginx, Redis, and PostgreSQL.

## Architecture
- **Reverse Proxy:** Nginx (Single external entry point on port 80)
- **Application Backend:** FastAPI (Multi-stage build, non-root user)
- **Cache / State:** Redis (In-memory hit counter)
- **Database:** PostgreSQL 16 (Data persistence via named volume)
- **Network:** Private, internal Docker bridge network

## Key Docker Features Implemented
1. **Multi-Stage Build:** Builders and compilers discarded; final image runs lightweight runtime.
2. **Security Hardening:** Non-root execution (`appuser:appgroup`), no direct external port exposure for database/cache.
3. **Resilient Startup:** Deterministic startup orchestration via `healthcheck` and `service_healthy` conditions.
4. **Data Persistence:** Database storage decoupled from container lifecycle via named volumes.

## Quickstart
```bash
git clone [https://github.com/](https://github.com/)<twoj-username>/docker-microservice.git
cd docker-microservice
docker compose up --build -d
