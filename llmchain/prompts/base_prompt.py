"""
llmchain/prompts/base_prompt.py

Defines the base interface for prompt templates in LLMChain.
"""
from abc import ABC, abstractmethod

class BasePrompt(ABC):
    @abstractmethod
    def format(self, **kwargs) -> str:
        """Format the prompt with given variables."""
        pass
