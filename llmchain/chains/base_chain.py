"""
llmchain/chains/base_chain.py

Defines the base interface for modular chains in LLMChain.
"""
from abc import ABC, abstractmethod

class BaseChain(ABC):
    @abstractmethod
    def run(self, input_data):
        """Run the chain with the given input and return the output."""
        pass

    @abstractmethod
    def add_step(self, step):
        """Add a step to the chain."""
        pass

    @abstractmethod
    def remove_step(self, step):
        """Remove a step from the chain."""
        pass
