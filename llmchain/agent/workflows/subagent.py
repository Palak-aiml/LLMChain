"""
llmchain/agent/workflows/subagent.py

Subagent management for complex workflows.
"""
class SubAgent:
    def __init__(self, name, act_fn):
        self.name = name
        self.act_fn = act_fn

    def act(self, input_data):
        return self.act_fn(input_data)

class SubAgentManager:
    def __init__(self):
        self.subagents = []

    def add_subagent(self, subagent):
        self.subagents.append(subagent)

    def remove_subagent(self, subagent):
        self.subagents.remove(subagent)

    def run_all(self, input_data):
        return [subagent.act(input_data) for subagent in self.subagents]
