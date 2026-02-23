"""
llmchain/embeddings/base_embedding.py

Defines the base interface for embedding models in LLMChain.
"""
from abc import ABC, abstractmethod

class BaseEmbedding(ABC):
    @abstractmethod
    def embed(self, text: str) -> list:
        """Embed a single string into a vector."""
        pass

    @abstractmethod
    def embed_batch(self, texts: list) -> list:
        """Embed a batch of strings into vectors."""
        pass
