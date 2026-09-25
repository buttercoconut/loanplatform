# Backend

This directory contains the FastAPI backend for the Loan Platform. It implements a simple loan application endpoint and a placeholder for loan review logic.

## Directory Layout

```
backend/
├─ app/
│  ├─ models/
│  │  └─ loan.py
│  ├─ routes/
│  │  └─ loan.py
│  ├─ services/
│  │  └─ loan.py
│  ├─ database/
│  │  └─ db.py
│  └─ main.py
├─ tests/
├─ Dockerfile
├─ requirements.txt
└─ README.md
```

## Running the Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.
