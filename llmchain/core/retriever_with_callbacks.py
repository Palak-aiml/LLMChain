"""
RetrieverWithCallbacks: A retriever that supports post-retrieval callbacks for logging, monitoring, or custom hooks.
"""
from typing import List, Callable, Any

class RetrieverWithCallbacks:
    def __init__(self, retriever, callbacks: List[Callable[[str, List[Any]], None]] = None):
        self.retriever = retriever
        self.callbacks = callbacks or []

    def retrieve(self, query: str) -> List[Any]:
        results = self.retriever.retrieve(query)
        for cb in self.callbacks:
            cb(query, results)
        return results

    def add_callback(self, callback: Callable[[str, List[Any]], None]):
        self.callbacks.append(callback)
