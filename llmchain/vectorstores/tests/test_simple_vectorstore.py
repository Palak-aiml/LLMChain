"""
llmchain/vectorstores/tests/test_simple_vectorstore.py

Unit tests for the SimpleVectorStore class.
"""
import unittest
from llmchain.vectorstores.simple_vectorstore import SimpleVectorStore

class TestSimpleVectorStore(unittest.TestCase):
    def test_add_and_search(self):
        store = SimpleVectorStore()
        store.add_vector([1.0, 0.0], metadata="A")
        store.add_vector([0.0, 1.0], metadata="B")
        store.add_vector([0.9, 0.1], metadata="C")
        results = store.search([1.0, 0.0], top_k=2)
        self.assertIn("A", results)
        self.assertIn("C", results)
        self.assertNotIn("B", results)

    def test_empty_search(self):
        store = SimpleVectorStore()
        results = store.search([1.0, 0.0])
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
