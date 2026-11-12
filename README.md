# prep-stock-api

Helps restaurant kitchens avoid running out of ingredients by suggesting daily prep quantities from recent usage and current stock.

## Why this project
A busy restaurant kitchen can serve over 500 customers a day while tracking around 35 stock lines. How much of each item to prep is usually decided by senior staff based on experience. If they underestimate, there may be no time to reorder, and a dish has to come off the menu. prep-stock-api records daily usage and suggests how much to prep, based on recent usage, current stock and a safety level for each item.

## Features
- [x] Add, view, update and delete stock items
- [x] Set a unit and a safety stock level for each item
- [x] Record daily usage
- [x] View usage history for an item over a date range
- [ ] Suggest how much to prep each day

## Tech stack
Python, FastAPI, SQLAlchemy 2.0, PostgreSQL, Alembic

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

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create the database
Open `psql` (or pgAdmin) and run:
```sql
CREATE DATABASE <database_name>;
```

### 5. Configure environment variables
Copy the example file, then open `.env` and fill in your PostgreSQL username, password and the database name you created in step 4:
```bash
copy .env.example .env       # Windows
cp .env.example .env         # macOS / Linux
```

### 6. Create the tables
Apply the database migrations with Alembic. This creates the `items` and `usage` tables:
```bash
alembic upgrade head
```

### 7. Run the server
```bash
uvicorn main:app --reload
```

Open http://localhost:8000/docs to try the API.

## API endpoints
| Method | Path | Description | Success | Errors |
|---|---|---|---|---|
| GET | /health | Check that the service is running | 200 | — |
| GET | /items | List all items | 200 | — |
| POST | /items | Create a new item (`unit` defaults to `bag`, `safety_stock` to 0) | 201 | 422 Invalid input |
| GET | /items/{id} | Get a single item by ID | 200 | 404 Item not found, 422 Invalid ID |
| PUT | /items/{id} | Replace an item's name, quantity, unit and safety stock (ID stays the same) | 200 | 404 Item not found, 422 Invalid input |
| DELETE | /items/{id} | Delete an item (only if it has no usage records) | 204 | 404 Item not found, 409 Item has usage records, 422 Invalid ID |
| POST | /usage | Record today's usage for an item (the date is set by the server) | 201 | 404 Item not found, 422 Invalid input |
| GET | /usage | List an item's usage over a date range, with item name and unit | 200 | 400 `start` is after `end`, 404 Item not found, 422 Invalid input |

### GET /usage query parameters
| Parameter | Required | Default | Example |
|---|---|---|---|
| `item_id` | Yes | — | `1` |
| `start` | No | 6 days before `end` | `2026-11-01` |
| `end` | No | Today | `2026-11-07` |

With no dates, it returns the last 7 days including today. Results are sorted by date. An item with no usage in the range returns an empty list.

## Data model

### items
| Column | Type | Notes |
|---|---|---|
| `id` | integer | Primary key |
| `name` | text | Item name |
| `quantity` | integer | Current stock |
| `unit` | text | Defaults to `bag` |
| `safety_stock` | integer | Minimum level to keep in stock; defaults to 0 |

### usage
| Column | Type | Notes |
|---|---|---|
| `id` | integer | Primary key |
| `item_id` | integer | Foreign key to `items.id` |
| `date` | date | Set by the server to today |
| `quantity` | integer | Bags used; must be greater than 0 |

One item can have many usage records (one-to-many).

## Design decisions
- **Usage is counted in whole bags.** Ingredients arrive from the central kitchen already packed, and an opened bag counts as one bag used, so `quantity` is an integer.
- **Staff can only record usage for today.** `POST /usage` does not accept a date; the server sets it. The rule lives in the API, not the database, so a future manager feature can add past records without changing the table.
- **Quantity must be greater than 0.** Checked twice: by Pydantic (returns 422) and by a database `CHECK` constraint (protects data written outside the API).
- **The API checks the item exists before saving usage.** The foreign key would also block it, but that surfaces as a 500 error; checking first returns a clear 404.
- **Items with usage records cannot be deleted.** Prep suggestions are calculated from past usage, so deleting that history would make them wrong. `DELETE /items/{id}` checks for usage first and returns 409 Conflict instead of letting the foreign key raise a 500 error.

## Out of scope (for now)
- **Manager permissions (correcting or back-filling usage).** Regular staff can only record today's usage. When a record is wrong or a day was missed, a manager would need to correct the record or add one for a past date. This needs login and role-based permissions, which are outside the current scope.

## Project status
In progress — week 9 of 26.
