"""
llmchain/memory/tests/test_memory.py

Unit tests for memory modules.
"""
import unittest
from llmchain.memory.simple_memory import SimpleMemory
from llmchain.memory.chat_memory import ChatMemory

class TestMemory(unittest.TestCase):
    def test_simple_memory(self):
        mem = SimpleMemory()
        mem.add("foo")
        mem.add("bar")
        self.assertEqual(mem.get(), ["foo", "bar"])

    def test_chat_memory(self):
        mem = ChatMemory()
        mem.add("user", "hello")
        mem.add("bot", "hi")
        self.assertEqual(mem.get(), [{"sender": "user", "message": "hello"}, {"sender": "bot", "message": "hi"}])

if __name__ == "__main__":
    unittest.main()
