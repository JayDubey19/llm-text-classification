baseline_prompt = """Classify the following text into toxic, spam, or safe:
{text}"""

improved_prompt = """You are a helpful moderation assistant.
Analyze the user text carefully and classify it as one of:
- toxic (offensive or hateful)
- spam (irrelevant or promotional)
- safe (harmless)

Text: {text}
Answer:"""
