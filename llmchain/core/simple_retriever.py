from .retriever_base import Retriever

class SimpleRetriever(Retriever):
    """A simple retriever that returns documents containing the query string."""
    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, query):
        return [doc for doc in self.documents if query.lower() in doc.content.lower()]
