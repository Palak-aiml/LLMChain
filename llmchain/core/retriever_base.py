from abc import ABC, abstractmethod

class Retriever(ABC):
    """Basic retriever interface for LLMChain."""
    @abstractmethod
    def retrieve(self, query):
        pass
