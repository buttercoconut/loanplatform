from .database import async_session
from .models import LoanApplicationDB
from sqlalchemy import select

async def create_loan_application(db, loan_data):
    db_loan = LoanApplicationDB(**loan_data)
    db.add(db_loan)
    await db.commit()
    await db.refresh(db_loan)
    return db_loan

async def get_loan_application(db, loan_id: int):
    result = await db.execute(select(LoanApplicationDB).where(LoanApplicationDB.id == loan_id))
    return result.scalar_one_or_none()
