"""
llmchain/core/agent_orchestrator.py

Advanced agent orchestration interface for LLMChain.
"""
from typing import List, Any, Callable

class AgentOrchestrator:
    def __init__(self, agents: List[Any], strategy: Callable[[List[Any], str], Any]):
        self.agents = agents
        self.strategy = strategy

    def run(self, input_text: str) -> Any:
        """Run the orchestration strategy with the given input."""
        return self.strategy(self.agents, input_text)

    def add_agent(self, agent: Any):
        self.agents.append(agent)

    def remove_agent(self, agent: Any):
        self.agents.remove(agent)
