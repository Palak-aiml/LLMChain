"""
llmchain/monitoring/tests/test_monitoring.py

Unit tests for monitoring, evaluation, and logging utilities.
"""
import unittest
from llmchain.monitoring.logger import Logger
from llmchain.monitoring.evaluator import Evaluator
from llmchain.monitoring.monitor import Monitor

class TestMonitoring(unittest.TestCase):
    def test_logger(self):
        Logger.setup()
        Logger.log("Test log message.")

    def test_evaluator(self):
        self.assertTrue(Evaluator.evaluate("foo", "foo"))
        self.assertFalse(Evaluator.evaluate("foo", "bar"))
        self.assertEqual(Evaluator.score("foo", "foo"), 1)
        self.assertEqual(Evaluator.score("foo", "bar"), 0)

    def test_monitor(self):
        monitor = Monitor()
        monitor.record_event("event1")
        monitor.record_event("event2")
        self.assertEqual(monitor.get_events(), ["event1", "event2"])

if __name__ == "__main__":
    unittest.main()
