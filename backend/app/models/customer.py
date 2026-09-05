from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    email: str
    income: float
    debt: float = 0.0

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    income: float
    debt: float
    class Config:
        orm_mode = True
