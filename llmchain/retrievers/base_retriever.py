"""
llmchain/retrievers/base_retriever.py

Defines the base interface for retrievers in LLMChain.
"""
from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> list:
        """Retrieve documents or items relevant to the query."""
        pass
