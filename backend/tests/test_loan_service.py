"""Unit tests for the loan service.

The tests use an in‑memory SQLite database to avoid external dependencies.
They cover the core decision logic: approval, rejection based on debt ratio
and amount.
"""

from __future__ import annotations

import os
import sys
import tempfile

from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure the backend package is importable
sys.path.append("/data/data/com.termux/files/home/project/md_templates/results/loanplatform/backend/app")

from database.database import Base
from services.loan_service import LoanService
from models.loan_application import LoanApplication

# Create a temporary SQLite database for tests
engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class TestLoanService:
    def test_approve_when_low_debt_and_small_amount(self, db_session):
        service = LoanService(db_session)
        payload = LoanApplication(
            customer_id=1,
            product_id=1,
            amount=100_000,
            term_months=12,
            income=120_000,
            debt_ratio=0.2,
        )
        app = service.create_application(payload)
        assert app.status == "APPROVED"

    def test_reject_when_high_debt(self, db_session):
        service = LoanService(db_session)
        payload = LoanApplication(
            customer_id=1,
            product_id=1,
            amount=100_000,
            term_months=12,
            income=120_000,
            debt_ratio=0.5,
        )
        app = service.create_application(payload)
        assert app.status == "REJECTED"

    def test_reject_when_large_amount(self, db_session):
        service = LoanService(db_session)
        payload = LoanApplication(
            customer_id=1,
            product_id=1,
            amount=600_000,
            term_months=12,
            income=120_000,
            debt_ratio=0.2,
        )
        app = service.create_application(payload)
        assert app.status == "REJECTED"
