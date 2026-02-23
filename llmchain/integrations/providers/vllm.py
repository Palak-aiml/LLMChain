"""
vLLM integration (stub).
"""
class VLLM:
    def __init__(self, api_key: str):
        self.api_key = api_key
    def generate(self, prompt: str, **kwargs):
        # Placeholder for vLLM API call
        return f"[vLLM] {prompt}"
