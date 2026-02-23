"""
llmchain/core/embeddings.py

Defines the base interface for embedding models in LLMChain.
"""
from abc import ABC, abstractmethod
from typing import List

class Embeddings(ABC):
    @abstractmethod
    def embed(self, text: str) -> List[float]:
        """Embed a single string into a vector."""
        pass

    @abstractmethod
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a batch of strings into vectors."""
        pass
