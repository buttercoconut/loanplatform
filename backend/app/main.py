from fastapi import FastAPI
from .routes import loan

app = FastAPI(title="Loan Platform API")
app.include_router(loan.router)
