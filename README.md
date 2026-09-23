"""
README for project.
"""
# Loan Platform

## Overview
This repository contains a minimal online loan platform built with FastAPI (backend) and Vue3 (frontend). It demonstrates a clean architecture with hexagonal design, PostgreSQL persistence, and a simple loan approval algorithm.

## Prerequisites
- Docker & Docker Compose
- Python 3.12+ (for local dev)
- Node 20+ (for local dev)

## Running locally
```bash
docker compose up --build
```

Backend API will be available at `http://localhost:8000`.
Frontend will be available at `http://localhost:5173`.

## API Endpoints
- `POST /loans/apply` – Submit a loan application.
- `GET /health` – Health check.

## Project Structure
```
backend/
  app/
    models/          # Pydantic & ORM models
    routes/          # FastAPI routers
    services/        # Business logic
    database/        # DB connection
  main.py
  Dockerfile
  requirements.txt
frontend/
  components/       # Vue components
  api/              # Axios wrappers
  router.js
  store/
  App.vue
  Dockerfile
  package.json
  vite.config.js
```

## Notes
- The loan approval logic is intentionally simple for demonstration.
- In production, replace the algorithm with a robust credit scoring service.
- Security features such as 2FA, encryption, and OWASP hardening are omitted for brevity.
