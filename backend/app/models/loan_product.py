from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str

class LoanProduct(BaseModel):
    id: int
    name: str
    max_amount: float
    min_amount: float
    max_term_months: int
    min_term_months: int
    base_interest_rate: float
