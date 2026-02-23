"""
llmchain/monitoring/advanced/tests/test_advanced_monitoring.py

Unit tests for advanced monitoring utilities.
"""
import unittest
from llmchain.monitoring.advanced.metrics import Metrics
from llmchain.monitoring.advanced.traces import Tracer
from llmchain.monitoring.advanced.dashboard import Dashboard
import time

class TestAdvancedMonitoring(unittest.TestCase):
    def test_metrics(self):
        m = Metrics()
        m.inc_counter("calls")
        m.set_gauge("active", 5)
        m.start_timer("latency")
        time.sleep(0.01)
        elapsed = m.stop_timer("latency")
        self.assertTrue(elapsed > 0)
        metrics = m.get_metrics()
        self.assertEqual(metrics["counters"]["calls"], 1)
        self.assertEqual(metrics["gauges"]["active"], 5)

    def test_tracer(self):
        t = Tracer()
        span = t.start_span("test")
        time.sleep(0.01)
        span.finish()
        traces = t.get_traces()
        self.assertEqual(traces[0]["name"], "test")
        self.assertTrue(traces[0]["duration"] > 0)

    def test_dashboard(self):
        d = Dashboard()
        d.metrics.inc_counter("foo")
        span = d.tracer.start_span("bar")
        time.sleep(0.01)
        span.finish()
        report = d.report()
        self.assertIn("metrics", report)
        self.assertIn("traces", report)

if __name__ == "__main__":
    unittest.main()
