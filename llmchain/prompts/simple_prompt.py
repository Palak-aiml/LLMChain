"""
llmchain/prompts/simple_prompt.py

A simple prompt template implementation.
"""
from .base_prompt import BasePrompt

class SimplePrompt(BasePrompt):
    def __init__(self, template: str):
        self.template = template

    def format(self, **kwargs) -> str:
        return self.template.format(**kwargs)
