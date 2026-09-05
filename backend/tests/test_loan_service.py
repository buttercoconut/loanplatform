import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_apply_loan_success():
    payload = {
        "customer_id": 1,
        "product_id": 1,
        "amount": 50000,
        "term_months": 24,
        "annual_income": 60000,
        "debt_to_income_ratio": 0.3,
        "credit_score": 720
    }
    response = client.post("/loans/apply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "approved"
    assert data["approved_amount"] > 0
