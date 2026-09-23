"""FastAPI router for loan‑application endpoints.

Only the minimal set of endpoints required for the MVP are implemented:

* POST /applications – create a new loan application.
* GET /applications/{id} – retrieve an existing application.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from ..database.database import get_db
from ..models.loan_application import LoanApplicationOut
from ..services.loan_service import LoanService

router = APIRouter(prefix="/applications", tags=["Loan Applications"])


@router.post("", response_model=LoanApplicationOut, status_code=status.HTTP_201_CREATED)
async def create_application(
    payload: LoanApplicationOut,
    db: Session = Depends(get_db),
):
    service = LoanService(db)
    application = service.create_application(payload)
    return application


@router.get("/{app_id}", response_model=LoanApplicationOut)
async def get_application(app_id: int, db: Session = Depends(get_db)):
    service = LoanService(db)
    application = service.get_application(app_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
