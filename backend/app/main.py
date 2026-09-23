"""FastAPI application entry point.

The app is configured with the router defined in `routes/loan_routes.py`.
Additional middleware (e.g. CORS, logging) can be added here.
"""

from __future__ import annotations

from fastapi import FastAPI

from .routes import loan_routes

app = FastAPI(title="Loan Platform API", version="0.1.0")

app.include_router(loan_routes.router)

# Simple health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
