"""
llmchain/plugins/example_plugin.py

Example plugin for LLMChain.
"""
from .base_plugin import BasePlugin

class ExamplePlugin(BasePlugin):
    def activate(self, app_context):
        print("ExamplePlugin activated!")

    def deactivate(self):
        print("ExamplePlugin deactivated!")
