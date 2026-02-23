"""
llmchain/chains/tests/test_modular_chain.py

Unit tests for the ModularChain class.
"""
import unittest
from llmchain.chains.modular_chain import ModularChain

class DummyStep:
    def __init__(self, suffix):
        self.suffix = suffix
    def run(self, data):
        return f"{data}-{self.suffix}"

class TestModularChain(unittest.TestCase):
    def test_chain(self):
        chain = ModularChain()
        step1 = DummyStep("A")
        step2 = DummyStep("B")
        chain.add_step(step1)
        chain.add_step(step2)
        result = chain.run("start")
        self.assertEqual(result, "start-A-B")
        chain.remove_step(step1)
        result2 = chain.run("start")
        self.assertEqual(result2, "start-B")

if __name__ == "__main__":
    unittest.main()
