"""
Advanced QA Chain: Supports retrieval-augmented question answering with LLMs and retrievers.
"""

from llmchain.llms.base import BaseLLM
from llmchain.retrievers.base import BaseRetriever
from llmchain.prompts.prompt_manager import PromptManager

class QAChain:
    def __init__(self, llm: BaseLLM, retriever: BaseRetriever, prompt_manager: PromptManager):
        self.llm = llm
        self.retriever = retriever
        self.prompt_manager = prompt_manager

    def run(self, question: str, context_docs=None, **kwargs):
        if context_docs is None:
            context_docs = self.retriever.retrieve(question)
        prompt = self.prompt_manager.build_qa_prompt(question, context_docs)
        return self.llm.generate(prompt, **kwargs)
