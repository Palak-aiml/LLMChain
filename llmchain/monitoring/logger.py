"""
llmchain/monitoring/logger.py

Logging utility for LLMChain.
"""
import logging

class Logger:
    @staticmethod
    def setup(level=logging.INFO):
        logging.basicConfig(
            level=level,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        logging.info("Logger initialized.")

    @staticmethod
    def log(message, level=logging.INFO):
        logging.log(level, message)
