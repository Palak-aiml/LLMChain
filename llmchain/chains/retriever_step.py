"""
llmchain/chains/retriever_step.py

Defines a chain step for document retrieval.
"""
class RetrieverChainStep:
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self, input_data):
        return self.retriever.retrieve(input_data)
