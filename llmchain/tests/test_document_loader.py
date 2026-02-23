import unittest
from llmchain.core.document_loader import DocumentLoader

class TestDocumentLoader(unittest.TestCase):
    def test_load(self):
        loader = DocumentLoader()
        doc = loader.load("Hello World", {"author": "test"})
        self.assertEqual(doc.content, "Hello World")
        self.assertEqual(doc.metadata["author"], "test")

if __name__ == "__main__":
    unittest.main()
