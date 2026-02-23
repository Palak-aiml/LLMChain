# LLMChain API Reference

This document provides an overview of the main modules, classes, and functions in LLMChain.

## Chains
- `llmchain.chains.advanced.QAChain`: Retrieval-augmented QA chain.
- `llmchain.chains.advanced.SummarizationChain`: Summarization chain.
- `llmchain.chains.advanced.ConversationalChain`: Multi-turn conversational chain.

## Agents
- `llmchain.agent.orchestration`: Agent orchestration and workflows.

## LLMs & Embeddings
- `llmchain.llms.openai_llm.OpenAILLM`: OpenAI LLM integration.
- `llmchain.llms.dummy_llm.DummyLLM`: Dummy/test LLM.
- `llmchain.embeddings.openai_embedding.OpenAIEmbedding`: OpenAI embedding integration.

## Vector Stores & Retrievers
- `llmchain.vectorstores.simple_vectorstore.SimpleVectorStore`: In-memory vector store.
- `llmchain.retrievers.simple_retriever.SimpleRetriever`: Simple retriever.

## Memory
- `llmchain.memory.chat_memory.ChatMemory`: Chat memory for conversations.
- `llmchain.memory.simple_memory.SimpleMemory`: Simple memory.

## Monitoring
- `llmchain.monitoring.experiment.ExperimentTracker`: Experiment tracking.
- `llmchain.monitoring.experiment.Debugger`: Debugging/logging.

## Plugins
- `llmchain.plugins.plugin_manager.PluginManager`: Plugin system.

## Enterprise
- `llmchain.enterprise.distributed_tracing`: Distributed tracing utilities.
- `llmchain.enterprise.security`: Security utilities.
- `llmchain.enterprise.scaling`: Scaling utilities.

## UI
- `ui.app`: FastAPI backend for visual builder and dashboard.

---
For detailed usage, see the README and module-level docstrings.
