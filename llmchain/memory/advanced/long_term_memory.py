"""
llmchain/memory/advanced/long_term_memory.py

Long-term memory for persistent agent state.
"""
import json
import os
from llmchain.memory.base_memory import BaseMemory

class LongTermMemory(BaseMemory):
    def __init__(self, filepath="long_term_memory.json"):
        self.filepath = filepath
        self.items = []
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.items = json.load(f)
        else:
            self.items = []
        return self.items

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.items, f)

    def add(self, item):
        self.items.append(item)
        self.save()

    def get(self):
        return self.items
