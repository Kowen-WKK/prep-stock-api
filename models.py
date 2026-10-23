from datetime import datetime
from decimal import Decimal
from sqlalchemy import Numeric, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    quantity: Mapped[Decimal] = mapped_column(Numeric, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )