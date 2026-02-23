"""
llmchain/integrations/community/chroma.py

Integration for Chroma vector store.
"""
import chromadb

class ChromaIntegration:
    def __init__(self, persist_directory=None):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("llmchain", metadata={"persist_directory": persist_directory} if persist_directory else None)

    def add(self, doc_id, embedding, metadata=None):
        self.collection.add(ids=[doc_id], embeddings=[embedding], metadatas=[metadata] if metadata else None)

    def query(self, embedding, top_k=5):
        results = self.collection.query(query_embeddings=[embedding], n_results=top_k)
        return results["ids"]
