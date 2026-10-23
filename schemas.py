from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class ItemCreate(BaseModel):   # 對方送進來的
    name: str = Field(min_length=1, max_length=50)
    quantity: float = Field(ge=0)

class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    quantity: float
    created_at: datetime