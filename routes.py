from database import get_db
from models import Item
from schemas import ItemCreate, ItemOut

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=list[ItemOut])
def list_items(db: Session = Depends(get_db)):
    return db.scalars(select(Item)).all()

@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = Item(name=payload.name, quantity=payload.quantity)
    db.add(item)      # 放進「訂單」
    db.commit()       # 簽名送出，這一刻才真正寫入
    db.refresh(item)  # 從資料庫拿回自動產生的 id
    return item

items_db = []

def find_item_or_404(item_id: int):
    # 在 items 裡找，找到就 return
    for item in items_db:
        if item.id == item_id:
            return item
    # 找不到就 raise HTTPException(status_code=404, ...)
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/{item_id}", response_model=ItemOut)
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