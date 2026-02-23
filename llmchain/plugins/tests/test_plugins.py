"""
llmchain/plugins/tests/test_plugins.py

Unit tests for plugin system.
"""
import unittest
from llmchain.plugins.plugin_manager import PluginManager
from llmchain.plugins.example_plugin import ExamplePlugin

class TestPlugins(unittest.TestCase):
    def test_plugin_lifecycle(self):
        manager = PluginManager()
        plugin = ExamplePlugin()
        manager.load_plugin(plugin)
        self.assertIn(plugin, manager.get_plugins())
        manager.unload_plugin(plugin)
        self.assertNotIn(plugin, manager.get_plugins())

if __name__ == "__main__":
    unittest.main()
