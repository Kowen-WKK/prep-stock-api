from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Item, Usage
from schemas import UsageCreate, UsageOut

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