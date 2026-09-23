"""Pydantic models for request/response schemas.

The models are split into two groups:

* `LoanApplicationCreate` – data required to create a new loan application.
* `LoanApplicationOut` – data returned to the client after creation.

Additional models for other entities can be added in the future.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class LoanApplicationCreate(BaseModel):
    """Schema for creating a new loan application.

    The fields are intentionally minimal for the MVP.  In a real system
    you would add more validation (e.g. credit score ranges, income
    thresholds, etc.).
    """

    customer_id: int = Field(..., description="Reference to the customer applying for the loan")
    product_id: int = Field(..., description="Reference to the loan product being requested")
    amount: float = Field(..., gt=0, description="Requested loan amount")
    term_months: int = Field(..., gt=0, description="Loan term in months")
    income: float = Field(..., gt=0, description="Annual income of the applicant")
    debt_ratio: float = Field(..., ge=0, le=1, description="Existing debt-to-income ratio (0-1)")

    @validator("debt_ratio")
    def debt_ratio_must_be_between_0_and_1(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("debt_ratio must be between 0 and 1")
        return v


class LoanApplicationOut(BaseModel):
    """Response schema for a loan application."""

    id: int
    customer_id: int
    product_id: int
    amount: float
    term_months: int
    income: float
    debt_ratio: float
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
