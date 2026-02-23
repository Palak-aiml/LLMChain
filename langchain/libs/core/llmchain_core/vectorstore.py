"""
llmchain/core/vectorstore.py

Defines the base interface for vector stores in LLMChain.
"""
from abc import ABC, abstractmethod
from typing import List, Any

class VectorStore(ABC):
    @abstractmethod
    def add_vector(self, vector: List[float], metadata: Any = None) -> None:
        """Add a vector and optional metadata to the store."""
        pass

    @abstractmethod
    def search(self, query_vector: List[float], top_k: int = 5) -> List[Any]:
        """Search for the top_k most similar vectors to the query_vector."""
        pass
