"""
llmchain/integrations/community/weaviate.py

Integration for Weaviate vector store.
"""
import weaviate

class WeaviateIntegration:
    def __init__(self, url, api_key=None):
        self.client = weaviate.Client(url=url, auth_client_secret=api_key)

    def add(self, class_name, properties):
        self.client.data_object.create(properties, class_name=class_name)

    def query(self, class_name, near_vector, top_k=5):
        result = self.client.query.get(class_name, ["*"]).with_near_vector({"vector": near_vector}).with_limit(top_k).do()
        return result["data"]["Get"][class_name]
