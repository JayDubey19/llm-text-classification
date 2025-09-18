import json
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from app.services.llm_service import classify_text

def load_dataset(path="eval/dataset.jsonl"):
    with open(path, "r") as f:
        return [json.loads(line) for line in f]

def evaluate():
    data = load_dataset()
    y_true, y_pred = [], []
    for item in data:
        y_true.append(item["label"])
        result = classify_text(item["text"])
        y_pred.append(result["class"])

    acc = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="macro")
    
    print("Accuracy:", acc)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)

if __name__ == "__main__":
    evaluate()
