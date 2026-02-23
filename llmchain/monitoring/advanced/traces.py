"""
llmchain/monitoring/advanced/traces.py

Tracing utility for LLMChain (simple span tracing).
"""
import time

class TraceSpan:
    def __init__(self, name):
        self.name = name
        self.start = time.time()
        self.end = None
        self.children = []

    def finish(self):
        self.end = time.time()

    def duration(self):
        return (self.end or time.time()) - self.start

class Tracer:
    def __init__(self):
        self.spans = []

    def start_span(self, name):
        span = TraceSpan(name)
        self.spans.append(span)
        return span

    def get_traces(self):
        return [{"name": s.name, "duration": s.duration()} for s in self.spans]
