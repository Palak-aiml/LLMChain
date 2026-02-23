"""
Reranker: Reranks retrieved documents based on a scoring function (e.g., LLM, embedding similarity).
"""
from typing import List, Callable

class Reranker:
    def __init__(self, score_fn: Callable[[str], float]):
        self.score_fn = score_fn

    def rerank(self, documents: List[str]) -> List[str]:
        return sorted(documents, key=self.score_fn, reverse=True)
