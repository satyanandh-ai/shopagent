# ShopAgent Backend

Initial FastAPI backend scaffold for ShopAgent.

## Requirements

- Python 3.11
- pip

## Setup on Windows (PowerShell)

From the repository root:

    py -3.11 -m venv backend/.venv
    & "./backend/.venv/Scripts/python.exe" -m pip install -r backend/requirements.txt

## Run the API

From the backend directory:

    & "./.venv/Scripts/python.exe" -m uvicorn app.main:app --reload

API: http://127.0.0.1:8000
Health: http://127.0.0.1:8000/health
Docs: http://127.0.0.1:8000/docs

## Run tests

From the backend directory:

    & "./.venv/Scripts/python.exe" -m pytest -v

## Current scope

- GET /health returns {"status": "ok"}.
- PostgreSQL and Redis are not connected.
- Database configuration, migrations, and application endpoints remain future work.
