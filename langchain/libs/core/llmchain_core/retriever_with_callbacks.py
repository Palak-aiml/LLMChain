"""
llmchain/core/retriever_with_callbacks.py

A retriever that supports callbacks for retrieval events.
"""
from typing import List, Any, Callable, Optional
from .retriever_with_embeddings import RetrieverWithEmbeddings

class RetrieverWithCallbacks(RetrieverWithEmbeddings):
    def __init__(self, embedding_model, vector_store, on_retrieve: Optional[Callable[[str, List[Any]], None]] = None):
        super().__init__(embedding_model, vector_store)
        self.on_retrieve = on_retrieve

    def retrieve(self, query: str, top_k: int = 5) -> List[Any]:
        results = super().retrieve(query, top_k=top_k)
        if self.on_retrieve:
            self.on_retrieve(query, results)
        return results
