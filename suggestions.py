from collections import defaultdict
from datetime import date, timedelta

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Item, Usage


def is_same_type(d: date, target: date) -> bool:
    """週六一組，其他日子一組"""
    return (d.weekday() == 5) == (target.weekday() == 5)


def pick_recent_days(daily_totals: dict[date, int], target: date, n: int = 4) -> list[date]:
    """從有紀錄的日子裡，挑出跟 target 同類、最近的 n 天"""
    same_type = sorted((d for d in daily_totals if is_same_type(d, target)), reverse=True)
    return same_type[:n]


def build_suggestions(db: Session, today: date) -> dict:
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    start = tomorrow - timedelta(weeks=8)

    # 8 週內，每個品項每天的總用量
    stmt = (
        select(Usage.item_id, Usage.used_on, func.sum(Usage.quantity))
        .where(Usage.used_on.between(start, yesterday))
        .group_by(Usage.item_id, Usage.used_on)
    )
    totals = defaultdict(dict)                  # {item_id: {日期: 總量}}
    for item_id, used_on, total in db.execute(stmt).all():
        totals[item_id][used_on] = total

    items = []
    for item in db.scalars(select(Item).order_by(Item.id)).all():
        daily = totals.get(item.id, {})
        days = pick_recent_days(daily, tomorrow)
        avg = round(sum(daily[d] for d in days) / len(days), 2) if days else None
        items.append({
            "item_id": item.id,
            "name": item.name,
            "unit": item.unit,
            "avg_usage": avg,
            "days_used": len(days),
            "based_on_dates": days,
        })

    return {
        "target_date": tomorrow,
        "day_type": "saturday" if tomorrow.weekday() == 5 else "other",
        "items": items,
    }