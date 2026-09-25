from pydantic import BaseModel
from typing import Optional

class LoanApplicationCreate(BaseModel):
    name: str
    email: str
    income: float
    loan_amount: float
    loan_term_months: int

class LoanApplicationResponse(BaseModel):
    id: int
    status: str
    created_at: str

class LoanApplicationStatusResponse(BaseModel):
    id: int
    status: str
    decision: Optional[str]
    score: Optional[int]
