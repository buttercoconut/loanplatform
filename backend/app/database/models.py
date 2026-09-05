from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LoanApplicationDB(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    income = Column(Float, nullable=False)
    debt_ratio = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    status = Column(String(20), default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)
