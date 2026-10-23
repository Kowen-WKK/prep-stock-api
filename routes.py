from fastapi import APIRouter, HTTPException
from schemas import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])

items_db = []
next_id = 1

def find_item_or_404(item_id: int):
    # 在 items 裡找，找到就 return
    for item in items_db:
        if item.id == item_id:
            return item
    # 找不到就 raise HTTPException(status_code=404, ...)
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("", response_model=list[Item])
def list_items():
    return items_db

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    return find_item_or_404(item_id)

@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    # 用 payload 的內容加上 next_id，組出一個 Item
    new_item = Item(id=next_id, **payload.model_dump())
    # 放進 items_db
    items_db.append(new_item)
    next_id += 1
    # 回傳剛建立的那個 Item
    return new_item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    item = find_item_or_404(item_id)
    # 用 payload 的內容更新這筆，id 保持不變
    for key, value in payload.model_dump().items():
        setattr(item, key, value)
    # return 更新後的那筆
    return item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    item = find_item_or_404(item_id)
    # 從 items 移除；不用 return'
    items_db.remove(item)