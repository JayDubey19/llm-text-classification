from transformers import pipeline
from app.prompts.prompts import baseline_prompt, improved_prompt

# Load Hugging Face model once at startup
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_text(text: str):
    """
    Runs the Hugging Face text classifier and maps output to categories.
    """

    # Run classification
    result = classifier(text, truncation=True, max_length=256)[0]

    # Map model labels (POSITIVE/NEGATIVE) to your categories
    # You can expand this mapping when using multi-class models
    label_map = {
        "POSITIVE": "safe",
        "NEGATIVE": "toxic"
    }
    predicted_class = label_map.get(result["label"], "safe")

    # Pick which prompt we used
    prompt = improved_prompt.format(text=text)

    return {
        "class": predicted_class,
        "confidence": round(result["score"], 2),
        "prompt": prompt
    }
