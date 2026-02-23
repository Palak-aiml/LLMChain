"""
llmchain/chains/tool_step.py

Defines a chain step for tool invocation.
"""
class ToolChainStep:
    def __init__(self, tool):
        self.tool = tool

    def run(self, input_data):
        return self.tool.execute(input_data)
