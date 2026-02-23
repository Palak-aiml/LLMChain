"""
llmchain/memory/advanced/episodic_memory.py

Episodic memory for session-based agent state.
"""
from llmchain.memory.base_memory import BaseMemory

class EpisodicMemory(BaseMemory):
    def __init__(self):
        self.episodes = []

    def load(self):
        return self.episodes

    def save(self):
        pass  # No-op for in-memory

    def add(self, episode):
        self.episodes.append(episode)

    def get(self):
        return self.episodes
