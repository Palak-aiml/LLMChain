"""
Advanced Summarization Chain: Summarizes documents using LLMs and prompt templates.
"""

from llmchain.llms.base import BaseLLM
from llmchain.prompts.prompt_manager import PromptManager

class SummarizationChain:
    def __init__(self, llm: BaseLLM, prompt_manager: PromptManager):
        self.llm = llm
        self.prompt_manager = prompt_manager

    def run(self, documents, **kwargs):
        prompt = self.prompt_manager.build_summarization_prompt(documents)
        return self.llm.generate(prompt, **kwargs)
