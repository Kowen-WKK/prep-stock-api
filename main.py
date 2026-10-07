from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items_db = []
next_id = 1

class ItemCreate(BaseModel):   # 對方送進來的
    name: str
    quantity: float

class Item(ItemCreate):        # 你存起來、回傳出去的
    id: int


@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

@app.get("/items", response_model = list[Item])
def list_items():
    return items_db

@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    # TODO 1: 用 payload 的內容加上 next_id，組出一個 Item
    new_item = Item(id=next_id, **payload.model_dump())
    # TODO 2: 放進 items_db
    items_db.append(new_item)
    # TODO 3: next_id 加 1
    next_id += 1
    # TODO 4: 回傳剛建立的那個 Item
    return new_item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")