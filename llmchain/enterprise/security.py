"""
Security: Basic API key authentication and input sanitization utilities.
"""
import os
import re
from functools import wraps

API_KEY = os.environ.get("LLMCHAIN_API_KEY", "changeme")

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = kwargs.get("api_key")
        if api_key != API_KEY:
            raise PermissionError("Invalid API key.")
        return func(*args, **kwargs)
    return wrapper

def sanitize_input(text):
    # Remove suspicious characters (basic example)
    return re.sub(r"[<>;]", "", text)
