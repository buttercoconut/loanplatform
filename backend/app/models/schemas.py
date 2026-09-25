# Pydantic schemas for API
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class CustomerOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    created_at: datetime

    class Config:
        orm_mode = True

class LoanProductOut(BaseModel):
    id: int
    name: str
    interest_rate: float
    max_amount: float
    min_credit_score: int
    created_at: datetime

    class Config:
        orm_mode = True

class LoanApplicationCreate(BaseModel):
    customer_id: int
    product_id: int
    amount: float
    income: float
    debt_ratio: float
    credit_score: int

class LoanApplicationOut(BaseModel):
    id: int
    customer_id: int
    product_id: int
    amount: float
    income: float
    debt_ratio: float
    credit_score: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
