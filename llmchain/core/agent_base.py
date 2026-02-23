from abc import ABC, abstractmethod

class Agent(ABC):
    """Basic agent interface for LLMChain."""
    @abstractmethod
    def act(self, input_data):
        pass
