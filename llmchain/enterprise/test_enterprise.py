import unittest
from llmchain.enterprise.distributed_tracing import trace_chain_step
from llmchain.enterprise.security import require_api_key, sanitize_input
from llmchain.enterprise.scaling import run_async, batch_process
import asyncio

class TestEnterpriseFeatures(unittest.TestCase):
    def test_trace_chain_step(self):
        @trace_chain_step("test_step")
        def dummy():
            return "traced"
        self.assertEqual(dummy(), "traced")

    def test_require_api_key(self):
        @require_api_key
        def protected(api_key=None):
            return "allowed"
        with self.assertRaises(PermissionError):
            protected(api_key="wrong")
        self.assertEqual(protected(api_key="changeme"), "allowed")

    def test_sanitize_input(self):
        dirty = "<script>alert('x')</script>;"
        clean = sanitize_input(dirty)
        self.assertNotIn("<", clean)
        self.assertNotIn(">", clean)
        self.assertNotIn(";", clean)

    def test_run_async(self):
        @run_async
        def sync_fn(x):
            return x + 1
        result = asyncio.run(sync_fn(1))
        self.assertEqual(result, 2)

    def test_batch_process(self):
        items = list(range(10))
        batches = list(batch_process(items, 3, lambda b: sum(b)))
        self.assertEqual(batches, [3, 12, 21, 9])

if __name__ == "__main__":
    unittest.main()
