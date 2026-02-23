"""
llmchain/tests/test_env_config.py

Unit tests for the EnvConfig class.
"""
import unittest
import os
from llmchain_core.env_config import EnvConfig

class TestEnvConfig(unittest.TestCase):
    def setUp(self):
        self.prefix = "LLMCHAIN_"
        self.config = EnvConfig(prefix=self.prefix)
        os.environ[self.prefix + "FOO"] = "bar"
        if self.prefix + "MISSING" in os.environ:
            del os.environ[self.prefix + "MISSING"]

    def tearDown(self):
        if self.prefix + "FOO" in os.environ:
            del os.environ[self.prefix + "FOO"]

    def test_get_existing(self):
        self.assertEqual(self.config.get("FOO"), "bar")

    def test_get_missing(self):
        self.assertIsNone(self.config.get("MISSING"))
        self.assertEqual(self.config.get("MISSING", default="baz"), "baz")

    def test_require_existing(self):
        self.assertEqual(self.config.require("FOO"), "bar")

    def test_require_missing(self):
        with self.assertRaises(RuntimeError):
            self.config.require("MISSING")

if __name__ == "__main__":
    unittest.main()
