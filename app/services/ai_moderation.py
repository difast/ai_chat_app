from transformers import pipeline
import os

class AIModerator:
    def __init__(self):
        self.model = pipeline(
            "text-classification", 
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def check_toxicity(self, text: str) -> bool:
        result = self.model(text)[0]
        return result["label"] == "NEGATIVE" and result["score"] > 0.9