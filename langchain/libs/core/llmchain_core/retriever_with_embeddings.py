"""
llmchain/core/retriever_with_embeddings.py

A retriever that uses an embedding model and a vector store to retrieve documents.
"""
from typing import List, Any
from .simple_embedding import SimpleEmbedding
from .simple_vectorstore import SimpleVectorStore

class RetrieverWithEmbeddings:
    def __init__(self, embedding_model: SimpleEmbedding, vector_store: SimpleVectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def add_document(self, text: str, metadata: Any = None):
        vector = self.embedding_model.embed(text)
        self.vector_store.add_vector(vector, metadata)

    def retrieve(self, query: str, top_k: int = 5) -> List[Any]:
        query_vector = self.embedding_model.embed(query)
        return self.vector_store.search(query_vector, top_k=top_k)
