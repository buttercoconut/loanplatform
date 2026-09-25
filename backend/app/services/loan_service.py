# Business logic for loan approval
from typing import Dict
from .database import SessionLocal, LoanApplication, LoanProduct

# Simple scoring thresholds
CREDIT_SCORE_THRESHOLD = 650
INCOME_DEBT_RATIO_THRESHOLD = 0.4


def evaluate_application(app: LoanApplication) -> Dict[str, str]:
    """Return decision and reason based on basic rules."""
    product = app.product
    # Check credit score
    if app.credit_score < product.min_credit_score:
        return {"status": "REJECTED", "reason": "Low credit score"}
    # Check debt ratio
    if app.debt_ratio > INCOME_DEBT_RATIO_THRESHOLD:
        return {"status": "REJECTED", "reason": "High debt ratio"}
    # Check amount vs max
    if app.amount > product.max_amount:
        return {"status": "REJECTED", "reason": "Amount exceeds product limit"}
    # If all good
    return {"status": "APPROVED", "reason": "All criteria met"}

# Service wrapper
class LoanService:
    def __init__(self, db):
        self.db = db

    def create_application(self, data):
        app = LoanApplication(**data)
        self.db.add(app)
        self.db.commit()
        self.db.refresh(app)
        # Evaluate immediately for MVP
        decision = evaluate_application(app)
        app.status = decision["status"]
        self.db.commit()
        self.db.refresh(app)
        return app

    def get_application(self, app_id: int):
        return self.db.query(LoanApplication).filter(LoanApplication.id == app_id).first()
