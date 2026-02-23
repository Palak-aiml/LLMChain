"""
llmchain/tests/test_retriever_with_callbacks.py

Unit tests for the RetrieverWithCallbacks class.
"""
import unittest
from llmchain_core.simple_embedding import SimpleEmbedding
from llmchain_core.simple_vectorstore import SimpleVectorStore
from llmchain_core.retriever_with_callbacks import RetrieverWithCallbacks

class TestRetrieverWithCallbacks(unittest.TestCase):
    def test_callback_invoked(self):
        emb = SimpleEmbedding()
        store = SimpleVectorStore()
        called = {}
        def callback(query, results):
            called['query'] = query
            called['results'] = results
        retriever = RetrieverWithCallbacks(emb, store, on_retrieve=callback)
        retriever.add_document("foo bar", metadata="doc1")
        retriever.retrieve("foo")
        self.assertEqual(called['query'], "foo")
        self.assertIn("doc1", called['results'])

    def test_no_callback(self):
        emb = SimpleEmbedding()
        store = SimpleVectorStore()
        retriever = RetrieverWithCallbacks(emb, store)
        retriever.add_document("baz qux", metadata="doc2")
        results = retriever.retrieve("baz")
        self.assertIn("doc2", results)

if __name__ == "__main__":
    unittest.main()
