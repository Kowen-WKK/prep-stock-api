from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import Numeric, Text, DateTime, func, CheckConstraint, ForeignKey
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
    unit: Mapped[str] = mapped_column(server_default="bag")
    safety_stock: Mapped[Decimal] = mapped_column(Numeric, server_default="0")


class Usage(Base):
    __tablename__ = "usage"
    __table_args__ = (
        CheckConstraint("quantity > 0", name="usage_quantity_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    used_on: Mapped[date] = mapped_column(server_default=func.current_date())
    quantity: Mapped[int]