from database import get_db
from datetime import date, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from models import Item, Usage
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import UsageCreate, UsageOut,UsageWithItem

router = APIRouter(prefix="/usage", tags=["usage"])


@router.post("", response_model=UsageOut, status_code=status.HTTP_201_CREATED)
def create_usage(payload: UsageCreate, db: Session = Depends(get_db)):
    # 1. 先確認品項存在
    item = db.get(Item, payload.item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # 2. 建立紀錄：日期由系統決定，只能是今天
    usage = Usage(
        item_id=payload.item_id,
        quantity=payload.quantity,
        used_on=date.today(),
    )

    # 3. 存進資料庫
    db.add(usage)
    db.commit()
    db.refresh(usage)

    return usage

@router.get("", response_model=list[UsageWithItem])
def list_usage(
    item_id: int,
    start: date | None = None,
    end: date | None = None,
    db: Session = Depends(get_db),
):
    # 1. 日期沒給就用預設值
    end = end or date.today()
    start = start or end - timedelta(days=6)

    # 2. 檢查 start 不能晚於 end
    if start > end:
        raise HTTPException(
            status_code=400,
            detail="start 不能晚於 end",
        )

    # 3. 檢查品項存在（跟 GET /items/{id} 一樣）
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    # 4. 組查詢、執行、回傳
    stmt = (
        select(Usage.used_on, Item.name, Usage.quantity, Item.unit)
        .join(Item, Usage.item_id == Item.id)
        .where(Usage.item_id == item_id)
        .where(Usage.used_on.between(start, end))
        .order_by(Usage.used_on)
    )
    return db.execute(stmt).mappings().all()