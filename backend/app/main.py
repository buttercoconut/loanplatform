from fastapi import FastAPI
from .routes import loan_routes

app = FastAPI(title="Loan Platform API")

app.include_router(loan_routes)

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
