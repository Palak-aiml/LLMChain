from .document import Document

class DocumentLoader:
    """Basic document loader for LLMChain."""
    def load(self, content, metadata=None):
        return Document(content, metadata)
