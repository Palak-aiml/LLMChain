"""
llmchain/integrations/community/huggingface.py

Integration for HuggingFace Transformers LLMs and embeddings.
"""
from transformers import pipeline

class HuggingFaceIntegration:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)
        self.embedder = pipeline("feature-extraction", model=model_name)

    def generate(self, prompt):
        result = self.generator(prompt, max_length=50)
        return result[0]["generated_text"]

    def embed(self, text):
        result = self.embedder(text)
        return result[0][0] if result else []
