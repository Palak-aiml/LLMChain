"""
llmchain/memory/advanced/tests/test_advanced_memory.py

Unit tests for advanced memory modules.
"""
import unittest
import os
from llmchain.memory.advanced.long_term_memory import LongTermMemory
from llmchain.memory.advanced.episodic_memory import EpisodicMemory
from llmchain.memory.advanced.retrieval_augmented_memory import RetrievalAugmentedMemory

class TestAdvancedMemory(unittest.TestCase):
    def test_long_term_memory(self):
        filepath = "test_long_term_memory.json"
        if os.path.exists(filepath):
            os.remove(filepath)
        mem = LongTermMemory(filepath)
        mem.add("foo")
        mem.add("bar")
        mem2 = LongTermMemory(filepath)
        self.assertEqual(mem2.get(), ["foo", "bar"])
        os.remove(filepath)

    def test_episodic_memory(self):
        mem = EpisodicMemory()
        mem.add(["step1", "step2"])
        self.assertEqual(mem.get(), [["step1", "step2"]])

    def test_retrieval_augmented_memory(self):
        mem = RetrievalAugmentedMemory()
        mem.add("hello world")
        mem.add("goodbye world")
        mem.add("hello there")
        results = mem.retrieve("hello", top_k=2)
        self.assertIn("hello world", results)
        self.assertIn("hello there", results)
        self.assertNotIn("goodbye world", results)

if __name__ == "__main__":
    unittest.main()
