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


def find_item_or_404(item_id: int):
    # 在 items 裡找，找到就 return
    for item in items_db:
        if item.id == item_id:
            return item
    # 找不到就 raise HTTPException(status_code=404, ...)
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

@app.get("/items", response_model = list[Item])
def list_items():
    return items_db

@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    # 用 payload 的內容加上 next_id，組出一個 Item
    new_item = Item(id=next_id, **payload.model_dump())
    # 放進 items_db
    items_db.append(new_item)
    next_id += 1
    # 回傳剛建立的那個 Item
    return new_item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return find_item_or_404(item_id)

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    item = find_item_or_404(item_id)
    # 用 payload 的內容更新這筆，id 保持不變
    for key, value in payload.model_dump().items():
        setattr(item, key, value)
    # return 更新後的那筆
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    item = find_item_or_404(item_id)
    # 從 items 移除；不用 return'
    items_db.remove(item)