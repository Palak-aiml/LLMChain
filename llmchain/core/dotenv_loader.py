"""
DotenvLoader: Standalone, reusable .env loader for config.
"""
from dotenv import load_dotenv
import os

class DotenvLoader:
    @staticmethod
    def load(env_file: str = ".env"):
        load_dotenv(env_file)
        return dict(os.environ)
