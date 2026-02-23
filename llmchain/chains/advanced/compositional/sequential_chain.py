"""
SequentialChain: Runs a sequence of chains in order, passing output to the next.
"""
from typing import List, Any

class SequentialChain:
    def __init__(self, chains: List):
        self.chains = chains

    def run(self, input_data: Any, **kwargs):
        data = input_data
        for chain in self.chains:
            data = chain.run(data, **kwargs)
        return data
