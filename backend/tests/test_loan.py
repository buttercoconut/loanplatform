# tests for loan application
import pytest
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_apply_loan_approved():
    payload = {
        "name": "홍길동",
        "income": 10000000,
        "debt": 1000000,
        "amount": 2000000
    }
    response = client.post("/api/loan/apply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "approved"
