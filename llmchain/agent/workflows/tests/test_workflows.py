"""
llmchain/agent/workflows/tests/test_workflows.py

Unit tests for agent workflows (planner, subagent, human-in-the-loop).
"""
import unittest
from llmchain.agent.workflows.planner import AgentPlanner
from llmchain.agent.workflows.subagent import SubAgent, SubAgentManager
from llmchain.agent.workflows.human_in_the_loop import HumanInTheLoop

class DummyStep:
    def run(self, data):
        return f"step:{data}"

class TestWorkflows(unittest.TestCase):
    def test_planner(self):
        steps = [DummyStep(), DummyStep()]
        planner = AgentPlanner(steps)
        planned = planner.plan("foo")
        self.assertEqual(planned, steps)
        result = planner.execute("foo")
        self.assertEqual(result, "step:step:foo")

    def test_subagent_manager(self):
        manager = SubAgentManager()
        sub1 = SubAgent("A", lambda x: f"A:{x}")
        sub2 = SubAgent("B", lambda x: f"B:{x}")
        manager.add_subagent(sub1)
        manager.add_subagent(sub2)
        results = manager.run_all("bar")
        self.assertIn("A:bar", results)
        self.assertIn("B:bar", results)
        manager.remove_subagent(sub1)
        results2 = manager.run_all("bar")
        self.assertNotIn("A:bar", results2)

    def test_human_in_the_loop(self):
        def prompt_fn(data):
            return f"Human reviewed: {data}"
        hitl = HumanInTheLoop(prompt_fn)
        result = hitl.review("baz")
        self.assertEqual(result, "Human reviewed: baz")

if __name__ == "__main__":
    unittest.main()
