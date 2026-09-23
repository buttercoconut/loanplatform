from fastapi import APIRouter, Depends
from ..models.loan import LoanApplication
from ..services.loan import process_application

router = APIRouter(prefix="/loan", tags=["loan"])

@router.post("/apply")
async def apply_loan(app: LoanApplication):
    result = await process_application(app)
    return result
