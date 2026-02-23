"""
llmchain/tests/test_simple_embedding.py

Unit tests for the SimpleEmbedding class.
"""
import unittest
from llmchain_core.simple_embedding import SimpleEmbedding

class TestSimpleEmbedding(unittest.TestCase):
    def test_embed(self):
        emb = SimpleEmbedding()
        vec = emb.embed("abc")
        self.assertEqual(len(vec), 3)
        self.assertAlmostEqual(vec[0], float(ord('a'))/255.0)
        self.assertAlmostEqual(vec[1], float(ord('b'))/255.0)
        self.assertAlmostEqual(vec[2], float(ord('c'))/255.0)

    def test_embed_empty(self):
        emb = SimpleEmbedding()
        vec = emb.embed("")
        self.assertEqual(vec, [0.0])

    def test_embed_batch(self):
        emb = SimpleEmbedding()
        batch = emb.embed_batch(["a", "bc"])
        self.assertEqual(len(batch), 2)
        self.assertEqual(batch[0], [float(ord('a'))/255.0])
        self.assertEqual(batch[1], [float(ord('b'))/255.0, float(ord('c'))/255.0])

if __name__ == "__main__":
    unittest.main()
