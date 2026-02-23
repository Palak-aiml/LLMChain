"""
DocumentCompressor: Compresses documents using an LLM or heuristic before retrieval/QA.
"""
from typing import List, Callable

class DocumentCompressor:
    def __init__(self, compressor_fn: Callable[[str], str]):
        self.compressor_fn = compressor_fn

    def compress(self, documents: List[str]) -> List[str]:
        return [self.compressor_fn(doc) for doc in documents]
