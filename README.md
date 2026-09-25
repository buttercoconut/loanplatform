# Loan Platform

This repository contains the full source code for the Loan Platform application, including both backend (FastAPI) and frontend (Vue3) components.

## Directory Layout

```
loan-platform/
├─ backend/          # FastAPI backend
│  ├─ app/           # Application code
│  │  ├─ models/     # Pydantic models
│  │  ├─ routes/     # API endpoints
│  │  ├─ services/   # Business logic
│  │  ├─ database/   # DB connection
│  │  └─ main.py     # FastAPI app
│  ├─ tests/         # Unit tests
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ README.md
├─ frontend/         # Vue3 frontend
│  ├─ src/           # Source files
│  │  ├─ api/        # Axios services
│  │  ├─ components/ # Vue components
│  │  ├─ views/      # Page components
│  │  ├─ store/      # Vuex store
│  │  ├─ router/     # Vue Router
│  │  ├─ main.js
│  │  └─ App.vue
│  ├─ index.html
│  ├─ vite.config.js
│  ├─ package.json
│  └─ README.md
└─ README.md
```

## Getting Started

Refer to the individual `README.md` files in the `backend` and `frontend` directories for setup instructions.
