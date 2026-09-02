from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class LoanApplication(BaseModel):
    applicant_id: int = Field(..., description="Unique ID of the applicant")
    loan_product_id: int = Field(..., description="ID of the loan product applied for")
    amount: float = Field(..., gt=0, description="Requested loan amount")
    income: float = Field(..., gt=0, description="Annual income of applicant")
    debt_ratio: float = Field(..., ge=0, le=1, description="Existing debt-to-income ratio")
    credit_score: int = Field(..., ge=300, le=850, description="Credit score from external agency")
    application_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="PENDING", description="Application status: PENDING, APPROVED, REJECTED")
