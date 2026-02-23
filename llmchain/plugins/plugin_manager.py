"""
llmchain/plugins/plugin_manager.py

Plugin manager for LLMChain.
"""
class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin):
        self.plugins.append(plugin)
        plugin.activate(self)

    def unload_plugin(self, plugin):
        plugin.deactivate()
        self.plugins.remove(plugin)

    def get_plugins(self):
        return self.plugins
