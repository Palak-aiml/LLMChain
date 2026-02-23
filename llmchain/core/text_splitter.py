class TextSplitter:
    """A simple text splitter for LLMChain."""
    def split(self, text, delimiter="\n"):
        return text.split(delimiter)
