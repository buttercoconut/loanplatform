import pytest
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_apply_loan_success():
    payload = {
        "applicant_id": 1,
        "loan_product_id": 101,
        "amount": 5000,
        "income": 20000,
        "debt_ratio": 0.2,
        "credit_score": 720
    }
    response = client.post("/loans/apply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == payload["applicant_id"]

def test_apply_loan_reject_high_amount():
    payload = {
        "applicant_id": 2,
        "loan_product_id": 102,
        "amount": 20000,
        "income": 20000,
        "debt_ratio": 0.3,
        "credit_score": 720
    }
    response = client.post("/loans/apply", json=payload)
    assert response.status_code == 400
