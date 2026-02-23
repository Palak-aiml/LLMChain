"""
llmchain/embeddings/dummy_embedding.py

A dummy embedding model for testing.
"""
from .base_embedding import BaseEmbedding

class DummyEmbedding(BaseEmbedding):
    def embed(self, text: str) -> list:
        return [float(ord(c))/255.0 for c in text] if text else [0.0]

    def embed_batch(self, texts: list) -> list:
        return [self.embed(t) for t in texts]
