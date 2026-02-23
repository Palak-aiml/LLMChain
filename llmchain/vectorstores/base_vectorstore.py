"""
llmchain/vectorstores/base_vectorstore.py

Defines the base interface for vector stores in LLMChain.
"""
from abc import ABC, abstractmethod

class BaseVectorStore(ABC):
    @abstractmethod
    def add_vector(self, vector: list, metadata=None):
        """Add a vector and optional metadata to the store."""
        pass

    @abstractmethod
    def search(self, query_vector: list, top_k: int = 5) -> list:
        """Search for the top_k most similar vectors to the query_vector."""
        pass
