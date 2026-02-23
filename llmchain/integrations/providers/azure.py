"""
Azure LLM integration (stub).
"""
class AzureLLM:
    def __init__(self, api_key: str):
        self.api_key = api_key
    def generate(self, prompt: str, **kwargs):
        # Placeholder for Azure API call
        return f"[Azure] {prompt}"
