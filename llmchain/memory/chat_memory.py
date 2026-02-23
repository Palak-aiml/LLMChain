"""
llmchain/memory/chat_memory.py

Chat history memory for stateful agents.
"""
from .base_memory import BaseMemory

class ChatMemory(BaseMemory):
    def __init__(self):
        self.messages = []

    def load(self):
        return self.messages

    def save(self):
        pass  # No-op for in-memory

    def add(self, sender, message):
        self.messages.append({"sender": sender, "message": message})

    def get(self):
        return self.messages
