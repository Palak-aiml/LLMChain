"""
llmchain/plugins/base_plugin.py

Base interface for LLMChain plugins.
"""
from abc import ABC, abstractmethod

class BasePlugin(ABC):
    @abstractmethod
    def activate(self, app_context):
        """Activate the plugin with the given application context."""
        pass

    @abstractmethod
    def deactivate(self):
        """Deactivate the plugin."""
        pass
