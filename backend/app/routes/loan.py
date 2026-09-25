from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.db import get_db
from ..models.loan import LoanApplicationCreate, LoanApplicationResponse, LoanApplicationStatusResponse
from ..services.loan import process_loan_application

router = APIRouter(prefix="/loan-applications", tags=["loan"])

@router.post("", response_model=LoanApplicationResponse)
async def submit_application(app: LoanApplicationCreate, db: Session = Depends(get_db)):
    try:
        result = process_loan_application(db, app)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("{app_id}/status", response_model=LoanApplicationStatusResponse)
async def get_status(app_id: int, db: Session = Depends(get_db)):
    # placeholder logic
    return LoanApplicationStatusResponse(id=app_id, status="PENDING", decision=None, score=None)
