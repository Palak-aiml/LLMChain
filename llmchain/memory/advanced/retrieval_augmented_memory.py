"""
llmchain/memory/advanced/retrieval_augmented_memory.py

Retrieval-augmented memory for semantic search over memory.
"""
from llmchain.memory.base_memory import BaseMemory
from llmchain.embeddings.dummy_embedding import DummyEmbedding
from llmchain.vectorstores.simple_vectorstore import SimpleVectorStore

class RetrievalAugmentedMemory(BaseMemory):
    def __init__(self, embedding_model=None, vector_store=None):
        self.embedding_model = embedding_model or DummyEmbedding()
        self.vector_store = vector_store or SimpleVectorStore()
        self.items = []

    def load(self):
        return self.items

    def save(self):
        pass  # No-op for in-memory

    def add(self, item):
        self.items.append(item)
        vector = self.embedding_model.embed(item)
        self.vector_store.add_vector(vector, item)

    def get(self):
        return self.items

    def retrieve(self, query, top_k=5):
        query_vector = self.embedding_model.embed(query)
        return self.vector_store.search(query_vector, top_k=top_k)
