"""
llmchain/tests/test_retriever_with_embeddings.py

Unit tests for the RetrieverWithEmbeddings class.
"""
import unittest
from llmchain_core.simple_embedding import SimpleEmbedding
from llmchain_core.simple_vectorstore import SimpleVectorStore
from llmchain_core.retriever_with_embeddings import RetrieverWithEmbeddings

class TestRetrieverWithEmbeddings(unittest.TestCase):
    def test_add_and_retrieve(self):
        emb = SimpleEmbedding()
        store = SimpleVectorStore()
        retriever = RetrieverWithEmbeddings(emb, store)
        retriever.add_document("hello world", metadata="doc1")
        retriever.add_document("goodbye world", metadata="doc2")
        retriever.add_document("hello there", metadata="doc3")
        results = retriever.retrieve("hello", top_k=2)
        self.assertIn("doc1", results)
        self.assertIn("doc3", results)
        self.assertNotIn("doc2", results)

    def test_empty_retrieve(self):
        emb = SimpleEmbedding()
        store = SimpleVectorStore()
        retriever = RetrieverWithEmbeddings(emb, store)
        results = retriever.retrieve("anything")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
