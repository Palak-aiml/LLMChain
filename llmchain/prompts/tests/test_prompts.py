"""
llmchain/prompts/tests/test_prompts.py

Unit tests for prompt engineering utilities.
"""
import unittest
from llmchain.prompts.simple_prompt import SimplePrompt
from llmchain.prompts.prompt_manager import PromptManager

class TestPrompts(unittest.TestCase):
    def test_simple_prompt(self):
        prompt = SimplePrompt("Hello, {name}!")
        result = prompt.format(name="Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_prompt_manager(self):
        manager = PromptManager()
        manager.add_prompt("greet", "Hi, {name}!")
        formatted = manager.format_prompt("greet", name="Bob")
        self.assertEqual(formatted, "Hi, Bob!")
        with self.assertRaises(ValueError):
            manager.format_prompt("unknown", name="Bob")

if __name__ == "__main__":
    unittest.main()
