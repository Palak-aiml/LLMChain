"""
llmchain/integrations/community/cohere.py

Integration for Cohere LLM and embeddings.
"""
import cohere

class CohereIntegration:
    def __init__(self, api_key):
        self.client = cohere.Client(api_key)

    def generate(self, prompt, model="command"):
        response = self.client.generate(
            model=model,
            prompt=prompt
        )
        return response.generations[0].text

    def embed(self, text, model="embed-english-v2.0"):
        response = self.client.embed(
            texts=[text],
            model=model
        )
        return response.embeddings[0]
