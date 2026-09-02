from fastapi import FastAPI
from .routes.loan_routes import router as loan_router

app = FastAPI(title="Loan Platform API")

app.include_router(loan_router)

# Create tables on startup
from .database.database import engine, Base

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
