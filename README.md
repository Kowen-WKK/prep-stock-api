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

## Getting started
TBD

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
In progress — week 4 of 26.