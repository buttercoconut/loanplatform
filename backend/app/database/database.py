from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/loan_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    income = Column(Float, nullable=False)
    debt = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class LoanProduct(Base):
    __tablename__ = "loan_products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    term_months = Column(Integer, nullable=False)

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    product_id = Column(Integer, ForeignKey("loan_products.id"))
    amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")
    credit_score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    customer = relationship("Customer")
    product = relationship("LoanProduct")

# Create tables
Base.metadata.create_all(bind=engine)
