from pydantic import BaseModel
from typing import Optional

class LoanApplication(BaseModel):
    name: str
    income: float
    debt: float
    amount: float
    credit_score: Optional[int] = None
    status: str = "pending"
