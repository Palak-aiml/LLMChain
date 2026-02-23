"""
llmchain/agent/workflows/planner.py

Agent planner for multi-step task planning and execution.
"""
class AgentPlanner:
    def __init__(self, steps):
        self.steps = steps

    def plan(self, input_data):
        # Example: return steps in order
        return self.steps

    def execute(self, input_data):
        data = input_data
        for step in self.steps:
            data = step.run(data)
        return data
