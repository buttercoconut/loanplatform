# Database connection and models
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/loan_platform")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Domain models
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # relationships
    applications = relationship("LoanApplication", back_populates="customer")

class LoanProduct(Base):
    __tablename__ = "loan_products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    interest_rate = Column(Float, nullable=False)
    max_amount = Column(Float, nullable=False)
    min_credit_score = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("loan_products.id"), nullable=False)
    amount = Column(Float, nullable=False)
    income = Column(Float, nullable=False)
    debt_ratio = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # relationships
    customer = relationship("Customer", back_populates="applications")
    product = relationship("LoanProduct")

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency for FastAPI
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
