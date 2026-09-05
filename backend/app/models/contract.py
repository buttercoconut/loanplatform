from pydantic import BaseModel

class ContractCreate(BaseModel):
    loan_application_id: int
    signed_at: str

class ContractResponse(BaseModel):
    id: int
    loan_application_id: int
    signed_at: str
    class Config:
        orm_mode = True
