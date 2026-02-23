"""
llmchain/agent/tests/test_orchestration.py

Unit tests for advanced agent orchestration.
"""
import unittest
from llmchain.agent.orchestration import AgentOrchestrator
from llmchain.agent.strategies import round_robin_strategy, voting_strategy, cascading_strategy

class DummyAgent:
    def __init__(self, name):
        self.name = name
    def act(self, input_text):
        return f"{self.name}-{input_text}"

class VotingAgent:
    def __init__(self, vote):
        self.vote = vote
    def act(self, input_text):
        return self.vote

class TestAgentOrchestration(unittest.TestCase):
    def test_round_robin(self):
        agents = [DummyAgent("A1"), DummyAgent("A2")]
        orchestrator = AgentOrchestrator(agents, round_robin_strategy)
        result = orchestrator.run("foo")
        self.assertEqual(result, ["A1-foo", "A2-foo"])

    def test_voting(self):
        agents = [VotingAgent("yes"), VotingAgent("no"), VotingAgent("yes")]
        orchestrator = AgentOrchestrator(agents, voting_strategy)
        result = orchestrator.run("bar")
        self.assertEqual(result, "yes")

    def test_cascading(self):
        agents = [DummyAgent("A1"), DummyAgent("A2")]
        orchestrator = AgentOrchestrator(agents, cascading_strategy)
        result = orchestrator.run("baz")
        self.assertEqual(result, "A2-A1-baz")

    def test_subagent_management(self):
        orchestrator = AgentOrchestrator([], round_robin_strategy)
        subagent = DummyAgent("Sub")
        orchestrator.add_subagent(subagent)
        self.assertIn(subagent, orchestrator.subagents)
        orchestrator.remove_subagent(subagent)
        self.assertNotIn(subagent, orchestrator.subagents)

    def test_history(self):
        agents = [DummyAgent("A1")]
        orchestrator = AgentOrchestrator(agents, round_robin_strategy)
        orchestrator.run("test")
        history = orchestrator.get_history()
        self.assertEqual(history[0]["input"], "test")

if __name__ == "__main__":
    unittest.main()
