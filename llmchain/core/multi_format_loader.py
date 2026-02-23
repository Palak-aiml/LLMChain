from .document import Document

class MultiFormatLoader:
    """Loader supporting multiple document formats."""
    def load(self, content, metadata=None, fmt="txt"):
        if fmt == "txt":
            return Document(content, metadata)
        elif fmt == "md":
            # For demonstration, treat markdown as plain text
            return Document(content, metadata)
        else:
            raise ValueError(f"Unsupported format: {fmt}")
