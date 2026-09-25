from fastapi import FastAPI
from app.routes.loan_routes import router as loan_router

app = FastAPI(title="Loan Platform API")

app.include_router(loan_router, prefix="/api/loans", tags=["loans"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
