from sqlalchemy.orm import Session
from ..database.models import LoanApplication
from ..models.loan import LoanApplicationCreate, LoanApplicationResponse

# Simple credit scoring logic

def calculate_score(app: LoanApplicationCreate) -> int:
    # Basic heuristic: higher income and lower loan amount -> higher score
    income_factor = app.income / 10000
    loan_factor = app.loan_amount / 10000
    score = int(income_factor - loan_factor)
    return max(0, min(100, score))

def process_loan_application(db: Session, app: LoanApplicationCreate) -> LoanApplicationResponse:
    # Persist application
    db_app = LoanApplication(
        name=app.name,
        email=app.email,
        income=app.income,
        loan_amount=app.loan_amount,
        loan_term_months=app.loan_term_months
    )
    db.add(db_app)
    db.commit()
    db.refresh(db_app)

    # Calculate score and set status
    score = calculate_score(app)
    db_app.status = "APPROVED" if score >= 50 else "REJECTED"
    db.commit()
    db.refresh(db_app)

    return LoanApplicationResponse(
        id=db_app.id,
        status=db_app.status,
        created_at=db_app.created_at.isoformat()
    )
