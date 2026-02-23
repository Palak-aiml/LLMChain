"""
llmchain/memory/base_memory.py

Defines the base interface for memory modules in LLMChain.
"""
from abc import ABC, abstractmethod

class BaseMemory(ABC):
    @abstractmethod
    def load(self):
        """Load memory state."""
        pass

    @abstractmethod
    def save(self):
        """Save memory state."""
        pass

    @abstractmethod
    def add(self, item):
        """Add an item to memory."""
        pass

    @abstractmethod
    def get(self):
        """Get memory contents."""
        pass
