"""
llmchain/llms/dummy_llm.py

A dummy LLM provider for testing.
"""
from .base_llm import BaseLLM

class DummyLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return f"Dummy response to: {prompt}"
