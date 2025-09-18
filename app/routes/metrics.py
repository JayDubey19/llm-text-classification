from fastapi import APIRouter
from app.telemetry.stats import stats

router = APIRouter()

@router.get("/")
def metrics():
    return stats.get_metrics()
