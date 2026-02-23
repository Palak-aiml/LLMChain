"""
Distributed Tracing: Integrates OpenTelemetry for tracing chains, agents, and LLM calls.
"""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
span_processor = BatchSpanProcessor(ConsoleSpanExporter())
tracer_provider.add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)

def trace_chain_step(step_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator
