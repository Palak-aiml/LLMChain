import unittest
from llmchain.core.example_agent import ExampleAgent

class TestExampleAgent(unittest.TestCase):
    def test_act(self):
        agent = ExampleAgent()
        result = agent.act("test input")
        self.assertEqual(result, "Echo: test input")

if __name__ == "__main__":
    unittest.main()
