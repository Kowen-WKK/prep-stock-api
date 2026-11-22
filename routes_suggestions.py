from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import SuggestionsOut
from suggestions import build_suggestions
from utils import today_london

router = APIRouter(prefix="/suggestions", tags=["suggestions"])


@router.get("", response_model=SuggestionsOut)
def get_suggestions(db: Session = Depends(get_db)):
    return build_suggestions(db, today_london())