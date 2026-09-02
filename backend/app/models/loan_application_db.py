from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class LoanApplicationDB(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, nullable=False)
    loan_product_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    income = Column(Float, nullable=False)
    debt_ratio = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    application_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="PENDING")

    # relationships can be added later (e.g., to Customer, LoanProduct)
