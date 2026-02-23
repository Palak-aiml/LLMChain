# AgentOrchestrator

Pluggable agent orchestration with strategy injection.

## Usage
```python
from llmchain.core.agent_orchestrator import AgentOrchestrator

def simple_strategy(*args, **kwargs):
    return "Agent result"

orchestrator = AgentOrchestrator(strategy=simple_strategy)
result = orchestrator.run()
```
