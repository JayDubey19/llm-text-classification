from fastapi import FastAPI
from app.routes import classify, feedback, metrics, healthz

app = FastAPI(title="LLM Text Classification API")

# Register routers
app.include_router(classify.router, prefix="/classify", tags=["classify"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
app.include_router(healthz.router, prefix="/healthz", tags=["healthz"])
