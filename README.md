# README for Loan Platform

## Overview
This repository contains a minimal loan application platform with a FastAPI backend and a Vue 3 frontend. The backend exposes endpoints for applying for a loan and checking application status. The frontend provides a simple form to submit loan applications.

## Directory Structure
```
loanplatform/
├─ backend/
│  ├─ app/
│  │  ├─ database/
│  │  ├─ models/
│  │  ├─ routes/
│  │  ├─ services/
│  │  ├─ main.py
│  │  └─ tests/
│  └─ Dockerfile
├─ frontend/
│  ├─ api/
│  ├─ components/
│  ├─ store/
│  ├─ main.js
│  └─ App.vue
├─ docker-compose.yml
└─ README.md
```

## Running Locally
```bash
# Build and start containers
docker compose up --build
```
The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:5173`.

## Testing
Backend tests can be run with:
```bash
cd backend/app
pytest
```

## Notes
- The backend uses SQLite for simplicity.
- The frontend uses Vite and Vue 3.
- API URL is configurable via `VUE_APP_API_URL`.
