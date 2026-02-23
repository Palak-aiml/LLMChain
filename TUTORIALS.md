# LLMChain Tutorials

## 1. Quick Start
```python
from llmchain.llms.dummy_llm import DummyLLM
llm = DummyLLM()
print(llm.generate("Hello, world!"))
```

## 2. Modular Chains
```python
from llmchain.chains.modular_chain import ModularChain
from llmchain.chains.llm_step import LLMChainStep
from llmchain.llms.dummy_llm import DummyLLM
chain = ModularChain()
chain.add_step(LLMChainStep(DummyLLM()))
print(chain.run("Chain input"))
```

## 3. Agent Orchestration
```python
from llmchain.agent.orchestration import AgentOrchestrator
from llmchain.agent.strategies import round_robin_strategy
class DummyAgent:
    def act(self, input_text):
        return f"Agent: {input_text}"
orchestrator = AgentOrchestrator([DummyAgent()], round_robin_strategy)
print(orchestrator.run("Test"))
```

## 4. Plugins
```python
from llmchain.plugins.plugin_manager import PluginManager
from llmchain.plugins.example_plugin import ExamplePlugin
manager = PluginManager()
plugin = ExamplePlugin()
manager.load_plugin(plugin)
manager.unload_plugin(plugin)
```
