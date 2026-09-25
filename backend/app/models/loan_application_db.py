from sqlalchemy import Column, Integer, Float, String
from ..database import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    term_months = Column(Integer, nullable=False)
    income = Column(Float, nullable=False)
    debt_ratio = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")
    approved_amount = Column(Float, nullable=True)
    interest_rate = Column(Float, nullable=True)
