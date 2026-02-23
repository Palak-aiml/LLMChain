# .env Config Loader

## Overview

`DotenvLoader` loads environment variables from a `.env` file into the process environment. This is useful for local development and configuration without hardcoding secrets or settings in code.

## Usage Example

```python
from llmchain_core.dotenv_loader import DotenvLoader

# Loads variables from .env in the current directory
DotenvLoader().load()

# Or specify a custom file
DotenvLoader(filepath="myenvfile").load()
```

Lines starting with `#` are ignored. Only lines with `KEY=VALUE` format are loaded.
