# LLM-Powered Text Classification API

A minimal **FastAPI-based API** for classifying text into categories such as **toxic**, **spam**, and **safe**, powered by a Hugging Face transformer model.  

This project was built as part of an assignment to demonstrate:
- LLM-powered content moderation
- Prompt engineering
- Feedback loop for continuous improvement
- API metrics & evaluation harness

---

## 🚀 Features
- **POST /classify** → Classify input text (`toxic`, `spam`, `safe`)
- **POST /feedback** → Store feedback for retraining/evaluation
- **GET /metrics** → Track total requests, class distribution, feedback, latency
- **GET /healthz** → Health check
- **Prompt Engineering** → Includes baseline and improved prompts
- **Evaluation Harness** → Accuracy, Precision, Recall, and F1 on small dataset

---

## 📂 Project Structure
```
.
├─ app/
│  ├─ main.py               # FastAPI entrypoint
│  ├─ routes/               # API route handlers
│  ├─ services/             # Hugging Face integration
│  ├─ prompts/              # Baseline & improved prompts
│  └─ telemetry/            # Metrics collection
├─ eval/
│  ├─ dataset.jsonl         # Small evaluation dataset
│  └─ run.py                # Evaluation script
├─ tests/
│  └─ test_api.py           # Basic API tests
├─ requirements.txt         # Dependencies
└─ README.md                # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/llm-text-classification.git
cd llm-text-classification
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
uvicorn app.main:app --reload
```

Visit 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test endpoints in Swagger UI.  

---

## 🛠️ API Usage

### 🔹 Health Check
```bash
GET /healthz
```
Response:
```json
{"status": "ok"}
```

### 🔹 Classify Text
```bash
POST /classify
{
  "text": "I hate you"
}
```
Response:
```json
{
  "class": "toxic",
  "confidence": 0.95,
  "prompt_used": "You are a helpful moderation assistant...\nText: I hate you\nAnswer:",
  "latency_ms": 120
}
```

### 🔹 Send Feedback
```bash
POST /feedback
{
  "text": "I hate you",
  "predicted": "toxic",
  "correct": "toxic"
}
```

### 🔹 Metrics
```bash
GET /metrics
```
Response example:
```json
{
  "total_requests": 3,
  "class_distribution": {"toxic": 2, "safe": 1},
  "feedback_counts": {"positive": 1, "negative": 0},
  "latency": {"avg_ms": 150, "p95_ms": 200}
}
```

---

## 🧠 Prompt Engineering

- **Baseline Prompt**
```text
Classify the following text into toxic, spam, or safe:
{text}
```

- **Improved Prompt**
```text
You are a helpful moderation assistant.
Analyze the user text carefully and classify it as one of:
- toxic (offensive or hateful)
- spam (irrelevant or promotional)
- safe (harmless)

Text: {text}
Answer:
```

**Choice Rationale:**  
- Baseline → zero-shot, minimal instruction.  
- Improved → role-based, structured categories, improves accuracy.  

---

## 📊 Evaluation

Dataset: [`eval/dataset.jsonl`](eval/dataset.jsonl) (~20–30 labeled examples).  

Run evaluation:
```bash
python -m eval.run
```

Metrics reported:
- Accuracy
- Precision
- Recall
- F1-score

---

## ⚖️ Design Trade-offs & Limitations
- **In-memory feedback** → resets on server restart (could be persisted in SQLite/JSON for production).
- **Small dataset** → only for demonstration, not robust training.
- **CPU inference only** → slower on large models, but works for assignment/demo.
- **Limited categories** → only `toxic`, `spam`, `safe`; can be expanded.

---

## 🌐 (Optional) Deployment
This API can be deployed to **Render**, **Railway**, or **Fly.io**.  
Start Command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## 🧪 Running Tests

This project includes basic tests for all endpoints using **pytest**.

### Run Tests
From the project root:
```bash
pytest
```

On Windows PowerShell, if you face `ModuleNotFoundError`, set `PYTHONPATH` explicitly:
```powershell
$env:PYTHONPATH="."; pytest
```

### Example Output
```
collected 4 items

tests/test_api.py ....                                                       [100%]

4 passed in 22.6s
```

✅ This confirms that `/healthz`, `/classify`, `/feedback`, and `/metrics` are all working as expected.

---

## ✅ Deliverables
- [x] FastAPI app with required endpoints  
- [x] Prompt library with baseline & improved prompts  
- [x] Feedback persistence  
- [x] Metrics endpoint  
- [x] Evaluation harness with dataset  
- [x] README with setup, usage, prompts, and evaluation  
- [x] Basic tests for endpoints  

---
