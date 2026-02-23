"""
EnvConfig: Structured environment variable manager for safe/typed config.
"""
import os
from dotenv import load_dotenv

class EnvConfig:
    def __init__(self, env_file: str = ".env"):
        load_dotenv(env_file)

    def get(self, key: str, default=None, cast_type=str):
        value = os.getenv(key, default)
        if value is not None and cast_type is not str:
            try:
                value = cast_type(value)
            except Exception:
                pass
        return value
