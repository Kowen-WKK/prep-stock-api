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

def find_item_or_404(db: Session, item_id: int) -> Item:
    item = db.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, data: ItemCreate, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in data.model_dump().items():
        setattr(item, key, value)   # 把新值一個個蓋上去
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = find_item_or_404(db,item_id)
    # 從 items 移除；不用 return'
    db.delete(item)
    db.commit()