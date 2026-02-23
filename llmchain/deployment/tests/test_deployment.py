"""
llmchain/deployment/tests/test_deployment.py

Unit tests for deployment utilities.
"""
import unittest
from llmchain.llms.dummy_llm import DummyLLM

class TestDeployment(unittest.TestCase):
    def test_dummy_llm(self):
        llm = DummyLLM()
        result = llm.generate("Deploy test")
        self.assertEqual(result, "Dummy response to: Deploy test")

if __name__ == "__main__":
    unittest.main()
