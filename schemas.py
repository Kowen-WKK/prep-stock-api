from pydantic import BaseModel, Field

class ItemCreate(BaseModel):   # 對方送進來的
    name: str = Field(min_length=1, max_length=50)
    quantity: float = Field(ge=0)

class Item(ItemCreate):        # 你存起來、回傳出去的
    id: int