from fastapi import APIRouter
from pydantic import BaseModel
from app.telemetry.stats import stats

router = APIRouter()

class FeedbackRequest(BaseModel):
    text: str
    predicted: str
    correct: str

@router.post("/")
def feedback(req: FeedbackRequest):
    is_positive = req.predicted == req.correct
    stats.record_feedback(is_positive)
    return {"status": "feedback recorded"}
