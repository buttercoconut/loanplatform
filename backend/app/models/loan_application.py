from pydantic import BaseModel, Field
from typing import Optional

class LoanApplicationCreate(BaseModel):
    customer_id: int
    product_id: int
    amount: float
    term_months: int
    income: float
    debt_ratio: float
    credit_score: int

class LoanApplicationResponse(BaseModel):
    id: int
    status: str
    approved_amount: Optional[float] = None
    interest_rate: Optional[float] = None
    message: Optional[str] = None

    class Config:
        orm_mode = True
