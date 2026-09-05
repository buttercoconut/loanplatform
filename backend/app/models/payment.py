from pydantic import BaseModel

class PaymentCreate(BaseModel):
    loan_application_id: int
    amount: float
    due_date: str

class PaymentResponse(BaseModel):
    id: int
    loan_application_id: int
    amount: float
    due_date: str
    paid_at: Optional[str]
    class Config:
        orm_mode = True
