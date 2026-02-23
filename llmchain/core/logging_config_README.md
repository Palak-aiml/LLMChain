# LoggingConfig

Centralized logging setup for LLMChain. Reads log level and format from .env or environment variables.

## Usage
```python
from llmchain.core.logging_config import LoggingConfig
LoggingConfig.setup_logging()
```

Set variables in your `.env`:
```
LLMCHAIN_LOG_LEVEL=DEBUG
LLMCHAIN_LOG_FORMAT=%(asctime)s - %(levelname)s - %(message)s
```
