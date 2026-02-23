"""
llmchain/tests/test_agent_orchestrator.py

Unit tests for the AgentOrchestrator class.
"""
import unittest
from llmchain_core.agent_orchestrator import AgentOrchestrator

class DummyAgent:
    def __init__(self, name):
        self.name = name
    def act(self, input_text):
        return f"{self.name} processed {input_text}"

def round_robin_strategy(agents, input_text):
    # Just call all agents and return their outputs
    return [agent.act(input_text) for agent in agents]

class TestAgentOrchestrator(unittest.TestCase):
    def setUp(self):
        self.agent1 = DummyAgent("A1")
        self.agent2 = DummyAgent("A2")
        self.orchestrator = AgentOrchestrator([self.agent1, self.agent2], round_robin_strategy)

    def test_run(self):
        result = self.orchestrator.run("foo")
        self.assertEqual(result, ["A1 processed foo", "A2 processed foo"])

    def test_add_remove_agent(self):
        agent3 = DummyAgent("A3")
        self.orchestrator.add_agent(agent3)
        result = self.orchestrator.run("bar")
        self.assertIn("A3 processed bar", result)
        self.orchestrator.remove_agent(agent3)
        result = self.orchestrator.run("baz")
        self.assertNotIn("A3 processed baz", result)

if __name__ == "__main__":
    unittest.main()
