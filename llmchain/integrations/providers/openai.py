"""
OpenAI LLM integration (stub).
"""
class OpenAILLM:
    def __init__(self, api_key: str):
        self.api_key = api_key
    def generate(self, prompt: str, **kwargs):
        # Placeholder for OpenAI API call
        return f"[OpenAI] {prompt}"
