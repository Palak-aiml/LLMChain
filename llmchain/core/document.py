class Document:
    """A simple document class for LLMChain."""
    def __init__(self, content, metadata=None):
        self.content = content
        self.metadata = metadata or {}

    def __repr__(self):
        return f"<Document content={self.content[:30]!r}... metadata={self.metadata}>"
