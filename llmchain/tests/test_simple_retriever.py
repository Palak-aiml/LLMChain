import unittest
from llmchain.core.document import Document
from llmchain.core.simple_retriever import SimpleRetriever

class TestSimpleRetriever(unittest.TestCase):
    def test_retrieve(self):
        docs = [Document("hello world"), Document("foo bar"), Document("worldwide web")]
        retriever = SimpleRetriever(docs)
        results = retriever.retrieve("world")
        self.assertEqual(len(results), 2)
        self.assertTrue(any("hello world" in doc.content for doc in results))
        self.assertTrue(any("worldwide web" in doc.content for doc in results))

if __name__ == "__main__":
    unittest.main()
