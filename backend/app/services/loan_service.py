"""Business logic for loan application processing.

The service layer contains the core decision‑making logic.  For the MVP we
implement a very simple credit‑score based rule set.  In a real system this
would be replaced by a call to an external credit‑rating service.
"""

from __future__ import annotations

from typing import Optional

from sqlalchemy.orm import Session

from ..models.loan_application import LoanApplication
from ..models import Base
from ..database.database import get_db


class LoanService:
    """Service class encapsulating loan‑application logic."""

    def __init__(self, db: Session):
        self.db = db

    def create_application(self, data) -> LoanApplication:
        """Persist a new loan application and run initial review.

        Parameters
        ----------
        data: pydantic model instance
            The validated request payload.
        """
        application = LoanApplication(
            customer_id=data.customer_id,
            product_id=data.product_id,
            amount=data.amount,
            term_months=data.term_months,
            income=data.income,
            debt_ratio=data.debt_ratio,
        )
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)

        # Run a simple credit check
        self._run_credit_check(application)
        return application

    def _run_credit_check(self, application: LoanApplication) -> None:
        """Very simple credit‑score simulation.

        The rule set is:
        * If debt_ratio > 0.4 -> reject
        * If amount > 500_000 -> reject
        * Otherwise approve
        """
        if application.debt_ratio > 0.4 or application.amount > 500_000:
            application.status = "REJECTED"
        else:
            application.status = "APPROVED"
        self.db.commit()

    def get_application(self, app_id: int) -> Optional[LoanApplication]:
        return self.db.query(LoanApplication).filter(LoanApplication.id == app_id).first()
