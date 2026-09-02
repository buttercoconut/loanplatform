from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.loan_application import LoanApplication
from ..services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/apply", response_model=LoanApplication)
async def apply_loan(app: LoanApplication, db: Session = Depends(get_db)):
    service = LoanService(db)
    result = service.apply(app)
    if not result:
        raise HTTPException(status_code=400, detail="Loan application failed")
    return result

@router.get("/status/{app_id}")
async def get_status(app_id: int, db: Session = Depends(get_db)):
    service = LoanService(db)
    status = service.get_status(app_id)
    if not status:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"app_id": app_id, "status": status}
