"""
llmchain/vectorstores/simple_vectorstore.py

A simple in-memory vector store implementation for LLMChain.
"""
from .base_vectorstore import BaseVectorStore
import math

class SimpleVectorStore(BaseVectorStore):
    def __init__(self):
        self.vectors = []  # List of (vector, metadata)

    def add_vector(self, vector: list, metadata=None):
        self.vectors.append((vector, metadata))

    def search(self, query_vector: list, top_k: int = 5) -> list:
        if not self.vectors:
            return []
        def cosine_similarity(a, b):
            dot = sum(x*y for x, y in zip(a, b))
            norm_a = math.sqrt(sum(x*x for x in a))
            norm_b = math.sqrt(sum(x*x for x in b))
            return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0
        scored = [
            (cosine_similarity(query_vector, vec), meta)
            for vec, meta in self.vectors
        ]
        scored.sort(reverse=True, key=lambda x: x[0])
        return [meta for _, meta in scored[:top_k]]
