"""
llmchain/chains/modular_chain.py

Implements a modular chain for combining multiple steps (LLMs, retrievers, tools, etc.).
"""
from .base_chain import BaseChain

class ModularChain(BaseChain):
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def remove_step(self, step):
        self.steps.remove(step)

    def run(self, input_data):
        data = input_data
        for step in self.steps:
            data = step.run(data)
        return data
