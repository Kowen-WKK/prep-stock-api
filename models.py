from pydantic import BaseModel

class ItemCreate(BaseModel):   # 對方送進來的
    name: str
    quantity: float

class Item(ItemCreate):        # 你存起來、回傳出去的
    id: int