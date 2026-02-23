"""
llmchain/core/simple_embedding.py

A simple embedding model that converts text to a vector using character ordinals.
"""
from typing import List
from .embeddings import Embeddings

class SimpleEmbedding(Embeddings):
    def embed(self, text: str) -> List[float]:
        # Simple embedding: normalize ord values of chars
        if not text:
            return [0.0]
        return [float(ord(c))/255.0 for c in text]

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        return [self.embed(t) for t in texts]
