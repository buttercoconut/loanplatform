"""
Unit tests for loan service.
"""
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.connection import Base

# Use in-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override dependency
from app.database.connection import get_db

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_apply_loan_approved():
    payload = {
        "customer_id": 1,
        "product_id": 101,
        "amount": 50000,
        "income": 120000,
        "debt": 20000,
        "credit_score": 720,
    }
    response = client.post("/api/v1/loan/apply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "APPROVED"
    assert data["approved_amount"] == 50000
    assert data["interest_rate"] == 0.04


def test_apply_loan_rejected_dti():
    payload = {
        "customer_id": 2,
        "product_id": 102,
        "amount": 30000,
        "income": 50000,
        "debt": 40000,  # high DTI
        "credit_score": 700,
    }
    response = client.post("/api/v1/loan/apply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "REJECTED"
    assert data["approved_amount"] is None
