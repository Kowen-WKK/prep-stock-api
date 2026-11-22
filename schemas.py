from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date


class ItemCreate(BaseModel):   # 對方送進來的
    name: str = Field(min_length=1, max_length=50)
    quantity: int = Field(ge=0)
    unit: str = "bag"
    safety_stock: int = Field(ge=0, default=0)

class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    quantity: int
    created_at: datetime
    unit: str
    safety_stock: int


class UsageCreate(BaseModel):      # 使用者送進來的
    item_id: int
    quantity: int = Field(gt=0)


class UsageOut(BaseModel):         # API 回傳出去的
    id: int
    item_id: int
    used_on: date
    quantity: int
    stock_after: int

    model_config = {"from_attributes": True}

class UsageWithItem(BaseModel):
    used_on: date
    name: str
    quantity: int
    unit: str


class SuggestionItem(BaseModel):
    item_id: int
    name: str
    unit: str
    avg_usage: float | None      # 8 週內沒紀錄 → null
    days_used: int
    based_on_dates: list[date]


class SuggestionsOut(BaseModel):
    target_date: date
    day_type: str                # "saturday" 或 "other"
    items: list[SuggestionItem]