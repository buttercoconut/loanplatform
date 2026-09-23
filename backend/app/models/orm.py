"""
SQLAlchemy ORM models.
"""
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    amount = Column(Float, nullable=False)
    term_months = Column(Integer, nullable=False)
    income = Column(Float, nullable=False)
    debt = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")
    approved_amount = Column(Float)
    interest_rate = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships can be added later
