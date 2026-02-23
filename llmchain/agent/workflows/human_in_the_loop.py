"""
llmchain/agent/workflows/human_in_the_loop.py

Human-in-the-loop workflow for agent decision making.
"""
class HumanInTheLoop:
    def __init__(self, prompt_fn):
        self.prompt_fn = prompt_fn

    def review(self, input_data):
        # Call prompt_fn to get human feedback
        return self.prompt_fn(input_data)
