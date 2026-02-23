"""
llmchain/retrievers/vectorstore_retriever.py

A retriever that uses an embedding model and a vector store for semantic search.
"""
from .base_retriever import BaseRetriever

class VectorStoreRetriever(BaseRetriever):
    def __init__(self, embedding_model, vector_store):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def add_document(self, text: str, metadata=None):
        vector = self.embedding_model.embed(text)
        self.vector_store.add_vector(vector, metadata)

    def retrieve(self, query: str, top_k: int = 5) -> list:
        query_vector = self.embedding_model.embed(query)
        return self.vector_store.search(query_vector, top_k=top_k)
