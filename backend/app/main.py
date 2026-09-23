from fastapi import FastAPI
from .routes import loan_routes

app = FastAPI(title="Loan Platform API")

# Include routers
app.include_router(loan_routes.router, prefix="/api/loans", tags=["Loans"])

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Loan Platform API"}
