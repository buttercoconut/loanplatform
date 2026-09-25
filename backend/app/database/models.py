from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .db import Base

class LoanApplication(Base):
    __tablename__ = 'loan_applications'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    income = Column(Float, nullable=False)
    loan_amount = Column(Float, nullable=False)
    loan_term_months = Column(Integer, nullable=False)
    status = Column(String, default='PENDING')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
