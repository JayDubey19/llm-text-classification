from fastapi import APIRouter
from pydantic import BaseModel
import time
from app.services.llm_service import classify_text
from app.telemetry.stats import stats

router = APIRouter()

class ClassifyRequest(BaseModel):
    text: str

@router.post("/")
def classify(req: ClassifyRequest):
    start = time.time()
    result = classify_text(req.text)
    latency = int((time.time() - start) * 1000)
    stats.record_request(result["class"], latency)
    return {
        "class": result["class"],
        "confidence": result["confidence"],
        "prompt_used": result["prompt"],
        "latency_ms": latency
    }
