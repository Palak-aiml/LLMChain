"""
llmchain/core/dotenv_loader.py

Loader for .env files to populate environment variables for LLMChain.
"""
import os
from typing import Optional

class DotenvLoader:
    def __init__(self, filepath: Optional[str] = None):
        self.filepath = filepath or ".env"

    def load(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())
