"""
llmchain/core/logging_config.py

Logging configuration utility for LLMChain.
"""
import logging
import os

class LoggingConfig:
    @staticmethod
    def configure():
        level = os.getenv("LLMCHAIN_LOG_LEVEL", "INFO").upper()
        fmt = os.getenv("LLMCHAIN_LOG_FORMAT", "%(asctime)s %(levelname)s %(name)s: %(message)s")
        logging.basicConfig(level=getattr(logging, level, logging.INFO), format=fmt)
