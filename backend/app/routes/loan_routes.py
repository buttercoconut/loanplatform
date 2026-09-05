from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.db import get_db
from ..models.loan_application import LoanApplicationCreate, LoanApplicationResponse
from ..services.loan_service import LoanApprovalService

router = APIRouter(prefix="/loans", tags=["loans"])

approval_service = LoanApprovalService()

@router.post("/apply", response_model=LoanApplicationResponse)
async def apply_loan(request: LoanApplicationCreate, db: Session = Depends(get_db)):
    # In real scenario, fetch customer and product from DB
    # Here we just simulate
    approved, amount, rate, msg = approval_service.evaluate(
        amount=request.amount,
        term_months=request.term_months,
        annual_income=request.annual_income,
        debt_to_income_ratio=request.debt_to_income_ratio,
        credit_score=request.credit_score,
    )
    if not approved:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    # Persist application (simplified)
    # Normally use ORM models; omitted for brevity
    return LoanApplicationResponse(
        application_id=1,
        status="approved",
        approved_amount=amount,
        interest_rate=rate,
        message=msg,
    )
