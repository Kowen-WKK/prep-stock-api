from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

LONDON = ZoneInfo("Europe/London")

def today_london() -> date:
    return datetime.now(LONDON).date()