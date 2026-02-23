"""
llmchain/embeddings/tests/test_embeddings.py

Unit tests for embedding models.
"""
import unittest
from llmchain.embeddings.dummy_embedding import DummyEmbedding

class TestEmbeddings(unittest.TestCase):
    def test_dummy_embedding(self):
        emb = DummyEmbedding()
        vec = emb.embed("abc")
        self.assertEqual(len(vec), 3)
        self.assertAlmostEqual(vec[0], float(ord('a'))/255.0)
        self.assertAlmostEqual(vec[1], float(ord('b'))/255.0)
        self.assertAlmostEqual(vec[2], float(ord('c'))/255.0)

if __name__ == "__main__":
    unittest.main()
