"""
llmchain/memory/simple_memory.py

A simple in-memory implementation for agent memory.
"""
from .base_memory import BaseMemory

class SimpleMemory(BaseMemory):
    def __init__(self):
        self.items = []

    def load(self):
        return self.items

    def save(self):
        pass  # No-op for in-memory

    def add(self, item):
        self.items.append(item)

    def get(self):
        return self.items
