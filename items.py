from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    count: int
    unit: str

ITEMS = [
    {"id": 1, "name": "Mochi XLB", "count": 8, "unit": "bag", "cost": 1.2},
    {"id": 2, "name": "Lava XLB", "count": 7, "unit": "bag"},
    {"id": 3, "name": "Pork XLB Filling", "count": 7, "unit": "bag"},
    {"id": 4, "name": "Chicken XLB Filling", "count": 30, "unit": "bag"}
    ]

@app.get("/items", response_model = list[Item])
def items():
    return ITEMS