# prep-stock-api

Helps restaurant kitchens avoid running out of ingredients by suggesting daily prep quantities from recent usage and current stock.

## Why this project
A busy restaurant kitchen can serve over 500 customers a day while tracking around 35 stock lines. How much of each item to prep is usually decided by senior staff based on experience. If they underestimate, there may be no time to reorder, and a dish has to come off the menu. prep-stock-api records daily usage and suggests how much to prep, based on recent usage, current stock and a safety level for each item.

## Features (planned)
- Add, view, update and delete stock items
- Set a safety stock level for each item
- Record daily usage
- Suggest how much to prep each day

## Tech stack
Python, FastAPI, PostgreSQL

## Getting Started

### Prerequisites

- Python 3.12
- PostgreSQL 17
- Git

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/prep-stock-api.git
cd prep-stock-api
```

### 2. Create a virtual environment and install dependencies

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows (PowerShell)
# source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the endpoints in the browser.

### 4. Set up the database

> **Note:** The API currently stores data in memory. Database integration is the next milestone — this step prepares the schema ahead of time.

```bash
psql -U postgres -c "CREATE DATABASE prep_stock;"
psql -U postgres -d prep_stock -f sql/01_create_items.sql
```

If `psql` is not recognised on Windows, add `C:\Program Files\PostgreSQL\17\bin` to your PATH and reopen the terminal.

## API endpoints
| Method | Path | Description | Success | Errors |
|---|---|---|---|---|
| GET | /health | Check that the service is running | 200 | — |
| GET | /items | List all items | 200 | — |
| POST | /items | Create a new item | 201 | 422 Invalid input |
| GET | /items/{id} | Get a single item by ID | 200 | 404 Item not found |

## Project status
In progress — week 5 of 26.