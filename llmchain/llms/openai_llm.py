"""
llmchain/llms/openai_llm.py

OpenAI LLM provider integration for LLMChain.
"""
import openai
from .base_llm import BaseLLM

class OpenAILLM(BaseLLM):
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def generate(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
