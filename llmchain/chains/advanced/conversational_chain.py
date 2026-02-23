"""
Conversational Chain: Handles multi-turn conversations with memory and LLMs.
"""

from llmchain.llms.base import BaseLLM
from llmchain.memory.base import BaseMemory
from llmchain.prompts.prompt_manager import PromptManager

class ConversationalChain:
    def __init__(self, llm: BaseLLM, memory: BaseMemory, prompt_manager: PromptManager):
        self.llm = llm
        self.memory = memory
        self.prompt_manager = prompt_manager

    def run(self, user_input: str, **kwargs):
        history = self.memory.get_history()
        prompt = self.prompt_manager.build_conversation_prompt(user_input, history)
        response = self.llm.generate(prompt, **kwargs)
        self.memory.append(user_input, response)
        return response
