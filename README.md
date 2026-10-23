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
​```bash
git clone https://github.com/<your-username>/prep-stock-api.git
cd prep-stock-api
​```

### 2. Create and activate a virtual environment
​```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
​```

### 3. Install dependencies
​```bash
pip install -r requirements.txt
​```

### 4. Create the database
Open `psql` (or pgAdmin) and run:
​```sql
CREATE DATABASE <database_name>;
​```

### 5. Configure environment variables
Copy the example file and fill in your own PostgreSQL password:
​```bash
copy .env.example .env       # Windows
cp .env.example .env         # macOS / Linux
​```

### 6. Run the server
​```bash
uvicorn <main:app> --reload
​```

Open http://localhost:8000/docs to try the API.

## API endpoints
| Method | Path | Description | Success | Errors |
|---|---|---|---|---|
| GET | /health | Check that the service is running | 200 | — |
| GET | /items | List all items | 200 | — |
| POST | /items | Create a new item | 201 | 422 Invalid input |
| GET | /items/{id} | Get a single item by ID | 200 | 404 Item not found |
| PUT | /items/{id} | Replace an item's name and quantity (ID stays the same) | 200 | 404 Item not found, 422 Invalid input |
| DELETE | /items/{id} | Delete an item | 204 | 404 Item not found |

## Project status
In progress — week 6 of 26.
