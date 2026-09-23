"""Database connection and ORM setup using SQLAlchemy and PostgreSQL.

This module provides a SQLAlchemy `engine`, `SessionLocal`, and a declarative
`Base` class that can be used by the rest of the application.  The connection
string is read from environment variables to keep secrets out of the code
base.  The module also exposes a `get_db` dependency that can be used in
FastAPI routes.

The database schema is defined in the `models` package.  Importing the
models here ensures that the tables are created when the application starts.
"""

from __future__ import annotations

import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load database URL from environment or use a default for local dev
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/loan_db")

# Create engine with pool_pre_ping to avoid stale connections
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# SessionLocal is a factory for new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Import models to register them with Base
# (This import must be after Base is defined)
from ..models import loan_application, customer, loan_product, contract, payment  # noqa: E402

# Create tables if they don't exist (useful for dev/testing)
Base.metadata.create_all(bind=engine)


# Dependency for FastAPI routes

def get_db() -> Generator:
    """Yield a database session and close it after use.

    FastAPI will call this dependency for each request that needs a DB
    connection.  It ensures that sessions are properly closed and that
    transactions are rolled back on error.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
