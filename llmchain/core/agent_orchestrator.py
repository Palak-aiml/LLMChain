"""
AgentOrchestrator: Pluggable agent orchestration with strategy injection.
"""
from typing import Callable, Any

class AgentOrchestrator:
    def __init__(self, strategy: Callable[[Any], Any]):
        self.strategy = strategy

    def run(self, *args, **kwargs):
        return self.strategy(*args, **kwargs)

    def set_strategy(self, strategy: Callable[[Any], Any]):
        self.strategy = strategy
