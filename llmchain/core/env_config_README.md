# EnvConfig

Structured environment variable manager for safe/typed config.

## Usage
```python
from llmchain.core.env_config import EnvConfig
config = EnvConfig()
api_key = config.get("OPENAI_API_KEY")
timeout = config.get("TIMEOUT", 30, int)
```
