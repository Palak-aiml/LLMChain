"""
llmchain/monitoring/advanced/metrics.py

Metrics collection for LLMChain (counters, timers, gauges).
"""
import time

class Metrics:
    def __init__(self):
        self.counters = {}
        self.timers = {}
        self.gauges = {}

    def inc_counter(self, name, value=1):
        self.counters[name] = self.counters.get(name, 0) + value

    def start_timer(self, name):
        self.timers[name] = time.time()

    def stop_timer(self, name):
        if name in self.timers:
            elapsed = time.time() - self.timers[name]
            self.gauges[name] = elapsed
            del self.timers[name]
            return elapsed
        return None

    def set_gauge(self, name, value):
        self.gauges[name] = value

    def get_metrics(self):
        return {"counters": self.counters, "gauges": self.gauges}
