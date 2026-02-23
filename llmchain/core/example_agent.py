from .agent_base import Agent

class ExampleAgent(Agent):
    """A simple example agent implementation."""
    def act(self, input_data):
        return f"Echo: {input_data}"
