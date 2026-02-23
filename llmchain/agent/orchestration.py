"""
llmchain/agent/orchestration.py

Advanced agent orchestration for LLMChain, supporting strategies like round-robin, voting, cascading, and subagent planning.
"""
from typing import List, Any, Callable

class AgentOrchestrator:
    def __init__(self, agents: List[Any], strategy: Callable[[List[Any], str], Any]):
        self.agents = agents
        self.strategy = strategy
        self.subagents = []
        self.history = []

    def run(self, input_text: str) -> Any:
        result = self.strategy(self.agents, input_text)
        self.history.append({"input": input_text, "result": result})
        return result

    def add_agent(self, agent: Any):
        self.agents.append(agent)

    def remove_agent(self, agent: Any):
        self.agents.remove(agent)

    def add_subagent(self, subagent: Any):
        self.subagents.append(subagent)

    def remove_subagent(self, subagent: Any):
        self.subagents.remove(subagent)

    def get_history(self):
        return self.history

    def set_strategy(self, strategy: Callable[[List[Any], str], Any]):
        self.strategy = strategy
