from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.schemas import LoanApplicationCreate, LoanApplicationOut
from ..services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/apply", response_model=LoanApplicationOut)
def apply_loan(data: LoanApplicationCreate, db: Session = Depends(get_db)):
    service = LoanService(db)
    app = service.create_application(data.dict())
    return app

@router.get("/{app_id}", response_model=LoanApplicationOut)
def get_loan(app_id: int, db: Session = Depends(get_db)):
    service = LoanService(db)
    app = service.get_application(app_id)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app
