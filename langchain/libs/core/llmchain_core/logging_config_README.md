# Logging Configuration

## Overview

`LoggingConfig` configures Python logging for LLMChain using environment variables:
- `LLMCHAIN_LOG_LEVEL`: Sets the log level (e.g., DEBUG, INFO).
- `LLMCHAIN_LOG_FORMAT`: Sets the log message format.

## Usage Example

```python
from llmchain_core.logging_config import LoggingConfig

LoggingConfig.configure()
```

Set environment variables before running to customize logging.
