"""
llmchain/tests/test_logging_config.py

Unit tests for the LoggingConfig utility.
"""
import unittest
import logging
import os
from llmchain_core.logging_config import LoggingConfig

class TestLoggingConfig(unittest.TestCase):
    def setUp(self):
        self.old_level = os.environ.get("LLMCHAIN_LOG_LEVEL")
        self.old_format = os.environ.get("LLMCHAIN_LOG_FORMAT")
        os.environ["LLMCHAIN_LOG_LEVEL"] = "DEBUG"
        os.environ["LLMCHAIN_LOG_FORMAT"] = "%(levelname)s: %(message)s"

    def tearDown(self):
        if self.old_level is not None:
            os.environ["LLMCHAIN_LOG_LEVEL"] = self.old_level
        else:
            if "LLMCHAIN_LOG_LEVEL" in os.environ:
                del os.environ["LLMCHAIN_LOG_LEVEL"]
        if self.old_format is not None:
            os.environ["LLMCHAIN_LOG_FORMAT"] = self.old_format
        else:
            if "LLMCHAIN_LOG_FORMAT" in os.environ:
                del os.environ["LLMCHAIN_LOG_FORMAT"]

    def test_configure(self):
        LoggingConfig.configure()
        logger = logging.getLogger("llmchain_test")
        logger.debug("debug message")
        logger.info("info message")
        # No assertion: just ensure no error and config applied

if __name__ == "__main__":
    unittest.main()
