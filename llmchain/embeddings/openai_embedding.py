"""
llmchain/embeddings/openai_embedding.py

OpenAI embedding model integration for LLMChain.
"""
import openai
from .base_embedding import BaseEmbedding

class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, api_key, model="text-embedding-ada-002"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def embed(self, text: str) -> list:
        response = openai.Embedding.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding

    def embed_batch(self, texts: list) -> list:
        response = openai.Embedding.create(
            model=self.model,
            input=texts
        )
        return [item.embedding for item in response.data]
