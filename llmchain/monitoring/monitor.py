"""
llmchain/monitoring/monitor.py

Monitoring utility for LLMChain.
"""
class Monitor:
    def __init__(self):
        self.events = []

    def record_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events
