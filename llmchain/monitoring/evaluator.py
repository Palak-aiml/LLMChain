"""
llmchain/monitoring/evaluator.py

Evaluation utility for LLMChain.
"""
class Evaluator:
    @staticmethod
    def evaluate(prediction, reference):
        return prediction == reference

    @staticmethod
    def score(prediction, reference):
        # Simple scoring: 1 if exact match, 0 otherwise
        return 1 if prediction == reference else 0
