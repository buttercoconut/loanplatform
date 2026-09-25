from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services import loan_service
from ..models import loan_application as schema
from ..database import get_db

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/apply", response_model=schema.LoanApplicationResponse)
def apply_loan(app: schema.LoanApplicationCreate, db: Session = Depends(get_db)):
    return loan_service.evaluate_application(db, app)
