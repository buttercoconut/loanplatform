# Service layer for loan logic
from ..models import loan_application as schema
from ..database import get_db
from sqlalchemy.orm import Session
from . import credit_service

# Simple scoring algorithm

def calculate_interest_rate(credit_score: int, debt_ratio: float) -> float:
    base_rate = 0.05
    if credit_score < 600:
        base_rate += 0.05
    elif credit_score < 700:
        base_rate += 0.03
    if debt_ratio > 0.4:
        base_rate += 0.02
    return base_rate


def evaluate_application(db: Session, app: schema.LoanApplicationCreate) -> schema.LoanApplicationResponse:
    # Basic validation
    if app.amount <= 0 or app.term_months <= 0:
        return schema.LoanApplicationResponse(
            id=0,
            status="REJECTED",
            message="Invalid amount or term"
        )
    # Simulate credit check
    credit_ok = credit_service.check_credit(app.customer_id, app.credit_score)
    if not credit_ok:
        return schema.LoanApplicationResponse(
            id=0,
            status="REJECTED",
            message="Credit check failed"
        )
    # Calculate interest
    rate = calculate_interest_rate(app.credit_score, app.debt_ratio)
    approved_amount = app.amount * 0.9  # 10% down
    # Persist
    new_app = schema.LoanApplicationDB(
        customer_id=app.customer_id,
        product_id=app.product_id,
        amount=app.amount,
        term_months=app.term_months,
        income=app.income,
        debt_ratio=app.debt_ratio,
        credit_score=app.credit_score,
        status="APPROVED",
        approved_amount=approved_amount,
        interest_rate=rate
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return schema.LoanApplicationResponse(
        id=new_app.id,
        status=new_app.status,
        approved_amount=approved_amount,
        interest_rate=rate,
        message="Approved"
    )
