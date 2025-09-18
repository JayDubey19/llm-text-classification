from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_classify():
    response = client.post("/classify/", json={"text": "I love coding"})
    assert response.status_code == 200
    data = response.json()
    assert "class" in data
    assert "confidence" in data
    assert "prompt_used" in data
    assert "latency_ms" in data

def test_feedback():
    response = client.post(
        "/feedback/",
        json={"text": "I love coding", "predicted": "safe", "correct": "safe"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "feedback recorded"}

def test_metrics():
    response = client.get("/metrics/")
    assert response.status_code == 200
    data = response.json()
    assert "total_requests" in data
    assert "class_distribution" in data
    assert "feedback_counts" in data
    assert "latency" in data
