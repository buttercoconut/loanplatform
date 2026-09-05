"""
API routes for loan operations.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.loan_service import review_loan
from app.models.loan_application import LoanApplicationCreate, LoanApplicationResponse
from app.database.connection import get_db

router = APIRouter()

@router.post("/apply", response_model=LoanApplicationResponse)
async def apply_loan(
    application: LoanApplicationCreate,
    db: Session = Depends(get_db),
):
    try:
        result = review_loan(application, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
