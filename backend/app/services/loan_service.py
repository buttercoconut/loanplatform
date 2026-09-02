from sqlalchemy.orm import Session
from ..models.loan_application_db import LoanApplicationDB
from ..models.loan_application import LoanApplication

class LoanService:
    def __init__(self, db: Session):
        self.db = db

    def apply(self, app: LoanApplication) -> LoanApplication:
        # Basic validation
        if app.amount > app.income * 0.5:
            return None
        # Simulate credit check
        if app.credit_score < 600:
            return None
        # Persist
        db_app = LoanApplicationDB(
            applicant_id=app.applicant_id,
            loan_product_id=app.loan_product_id,
            amount=app.amount,
            income=app.income,
            debt_ratio=app.debt_ratio,
            credit_score=app.credit_score,
            status="APPROVED",
        )
        self.db.add(db_app)
        self.db.commit()
        self.db.refresh(db_app)
        return app

    def get_status(self, app_id: int) -> str:
        db_app = self.db.query(LoanApplicationDB).filter_by(id=app_id).first()
        return db_app.status if db_app else None
