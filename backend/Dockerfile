"""Dockerfile for the FastAPI backend.

The image is based on the official Python slim image and installs the
requirements from `requirements.txt`.  The application is started with
uvicorn.
"""

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
