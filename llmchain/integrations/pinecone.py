"""
llmchain/integrations/pinecone.py

Integration for Pinecone vector store.
"""
import pinecone

class PineconeIntegration:
    def __init__(self, api_key, environment):
        pinecone.init(api_key=api_key, environment=environment)

    def create_index(self, name, dimension):
        return pinecone.create_index(name, dimension=dimension)

    def get_index(self, name):
        return pinecone.Index(name)

    def upsert(self, index, vectors):
        index.upsert(vectors)

    def query(self, index, vector, top_k=5):
        return index.query(vector, top_k=top_k)
