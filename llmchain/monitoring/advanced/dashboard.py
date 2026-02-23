"""
llmchain/monitoring/advanced/dashboard.py

Simple dashboard utility for LLMChain metrics and traces.
"""
from llmchain.monitoring.advanced.metrics import Metrics
from llmchain.monitoring.advanced.traces import Tracer

class Dashboard:
    def __init__(self):
        self.metrics = Metrics()
        self.tracer = Tracer()

    def report(self):
        return {
            "metrics": self.metrics.get_metrics(),
            "traces": self.tracer.get_traces()
        }
