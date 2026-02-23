"""
ConversationalRetrievalQAChain: Combines conversational memory with retrieval QA.
"""
from llmchain.llms.base import BaseLLM
from llmchain.memory.base import BaseMemory
from llmchain.retrievers.base import BaseRetriever
from llmchain.prompts.prompt_manager import PromptManager

class ConversationalRetrievalQAChain:
    def __init__(self, llm: BaseLLM, memory: BaseMemory, retriever: BaseRetriever, prompt_manager: PromptManager):
        self.llm = llm
        self.memory = memory
        self.retriever = retriever
        self.prompt_manager = prompt_manager

    def run(self, question: str, **kwargs):
        history = self.memory.get_history()
        context_docs = self.retriever.retrieve(question)
        prompt = self.prompt_manager.build_conversational_qa_prompt(question, history, context_docs)
        answer = self.llm.generate(prompt, **kwargs)
        self.memory.append(question, answer)
        return answer
