"""
Pydantic models for API payloads.
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class LoanApplicationCreate(BaseModel):
    customer_id: int
    product_id: int
    amount: float
    term_months: int
    income: float
    debt: float
    credit_score: int

class LoanApplicationResponse(BaseModel):
    id: int
    status: str
    approved_amount: Optional[float] = None
    interest_rate: Optional[float] = None
    created_at: datetime

    class Config:
        orm_mode = True
