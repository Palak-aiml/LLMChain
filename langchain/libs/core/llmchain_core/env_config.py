"""
llmchain/core/env_config.py

Environment variable-based configuration loader for LLMChain.
"""
import os
from typing import Any, Optional

class EnvConfig:
    def __init__(self, prefix: str = "LLMCHAIN_"):
        self.prefix = prefix

    def get(self, key: str, default: Optional[Any] = None) -> Optional[str]:
        return os.getenv(self.prefix + key, default)

    def require(self, key: str) -> str:
        value = os.getenv(self.prefix + key)
        if value is None:
            raise RuntimeError(f"Required environment variable {self.prefix + key} not set")
        return value
