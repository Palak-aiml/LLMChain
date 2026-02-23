"""
llmchain/llms/tests/test_llms.py

Unit tests for LLM providers.
"""
import unittest
from llmchain.llms.dummy_llm import DummyLLM

class TestLLMs(unittest.TestCase):
    def test_dummy_llm(self):
        llm = DummyLLM()
        result = llm.generate("Hello")
        self.assertEqual(result, "Dummy response to: Hello")

if __name__ == "__main__":
    unittest.main()
