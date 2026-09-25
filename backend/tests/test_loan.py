# tests/test_loan.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def loan_payload():
    return {
        "name": "홍길동",
        "email": "hong@example.com",
        "income": 50000000,
        "loan_amount": 20000000,
        "loan_term_months": 24
    }

def test_submit_application(loan_payload):
    response = client.post("/loan-applications", json=loan_payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["status"] in ["APPROVED", "REJECTED"]

def test_get_status(loan_payload):
    # First create
    resp = client.post("/loan-applications", json=loan_payload)
    app_id = resp.json()["id"]
    status_resp = client.get(f"/loan-applications/{app_id}/status")
    assert status_resp.status_code == 200
    status_data = status_resp.json()
    assert status_data["id"] == app_id
    assert status_data["status"] in ["APPROVED", "REJECTED", "PENDING"]
