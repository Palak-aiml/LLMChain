"""
llmchain/core/simple_vectorstore.py

A simple in-memory implementation of the VectorStore interface.
"""
from typing import List, Any, Tuple
from .vectorstore import VectorStore
import numpy as np

class SimpleVectorStore(VectorStore):
    def __init__(self):
        self.vectors: List[Tuple[List[float], Any]] = []

    def add_vector(self, vector: List[float], metadata: Any = None) -> None:
        self.vectors.append((vector, metadata))

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Any]:
        if not self.vectors:
            return []
        # Compute cosine similarity
        def cosine_similarity(a, b):
            a = np.array(a)
            b = np.array(b)
            return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
        scored = [
            (cosine_similarity(query_vector, vec), meta)
            for vec, meta in self.vectors
        ]
        scored.sort(reverse=True, key=lambda x: x[0])
        return [meta for _, meta in scored[:top_k]]
