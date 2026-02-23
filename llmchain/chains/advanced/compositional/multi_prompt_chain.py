"""
MultiPromptChain: Routes input to different prompt chains based on a selector.
"""
from typing import Dict, Callable

class MultiPromptChain:
    def __init__(self, prompt_chains: Dict[str, Callable], selector: Callable[[str], str]):
        self.prompt_chains = prompt_chains
        self.selector = selector

    def run(self, input_text: str, **kwargs):
        key = self.selector(input_text)
        chain = self.prompt_chains.get(key)
        if not chain:
            raise ValueError(f"No chain found for selector key: {key}")
        return chain.run(input_text, **kwargs)
