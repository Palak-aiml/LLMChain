"""
llmchain/chains/llm_step.py

Defines a chain step for LLM inference.
"""
class LLMChainStep:
    def __init__(self, llm):
        self.llm = llm

    def run(self, input_data):
        return self.llm.generate(input_data)
