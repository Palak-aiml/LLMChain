# Agent Orchestration

## Overview

`AgentOrchestrator` enables advanced orchestration of multiple agents using a user-defined strategy. Agents can be added or removed dynamically, and the orchestration logic is fully customizable.

## Usage Example

```python
from llmchain_core.agent_orchestrator import AgentOrchestrator

def my_strategy(agents, input_text):
    # Example: call all agents and collect results
    return [agent.act(input_text) for agent in agents]

orchestrator = AgentOrchestrator([agent1, agent2], my_strategy)
result = orchestrator.run("hello")
```

You can implement any orchestration logic, such as round-robin, voting, or cascading calls.
