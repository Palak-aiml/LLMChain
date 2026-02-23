"""
llmchain/retrievers/tests/test_vectorstore_retriever.py

Unit tests for the VectorStoreRetriever class.
"""
import unittest
from llmchain.embeddings.dummy_embedding import DummyEmbedding
from llmchain.vectorstores.simple_vectorstore import SimpleVectorStore
from llmchain.retrievers.vectorstore_retriever import VectorStoreRetriever

class TestVectorStoreRetriever(unittest.TestCase):
    def test_add_and_retrieve(self):
        emb = DummyEmbedding()
        store = SimpleVectorStore()
        retriever = VectorStoreRetriever(emb, store)
        retriever.add_document("hello world", metadata="doc1")
        retriever.add_document("goodbye world", metadata="doc2")
        retriever.add_document("hello there", metadata="doc3")
        results = retriever.retrieve("hello", top_k=2)
        self.assertIn("doc1", results)
        self.assertIn("doc3", results)
        self.assertNotIn("doc2", results)

    def test_empty_retrieve(self):
        emb = DummyEmbedding()
        store = SimpleVectorStore()
        retriever = VectorStoreRetriever(emb, store)
        results = retriever.retrieve("anything")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
