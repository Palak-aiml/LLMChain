"""
LoggingConfig: Centralized logging setup with .env/env var support.
"""
import logging
import os
from dotenv import load_dotenv

class LoggingConfig:
    @staticmethod
    def setup_logging():
        load_dotenv()
        log_level = os.getenv("LLMCHAIN_LOG_LEVEL", "INFO").upper()
        log_format = os.getenv("LLMCHAIN_LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")
        logging.basicConfig(level=log_level, format=log_format)
