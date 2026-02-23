# LLMChain Documentation

LLMChain is a modular framework for building agents and LLM-powered applications. It supports agent orchestration, multiple LLM providers, embeddings, vector stores, retrievers, memory, prompt engineering, monitoring, evaluation, logging, and production deployment.

## Features
- Modular chains for flexible workflows
- Advanced agent orchestration (round-robin, voting, cascading, subagents)
- Multiple LLM providers (OpenAI, dummy)
- Embedding models (OpenAI, dummy)
- Vector stores and retrievers (in-memory, semantic search)
- Memory modules (generic, chat history)
- Prompt engineering utilities
- Monitoring, evaluation, and logging
- Production deployment (FastAPI server, CLI)

## Quick Start
1. Install dependencies:
   ```bash
   pip install fastapi openai
   ```
2. Run the FastAPI server:
   ```bash
   python llmchain/deployment/server.py
   ```
3. Use the CLI:
   ```bash
   python llmchain/deployment/cli.py "Your prompt here"
   ```

## Contributing
- Fork the repo, create a branch, and submit a pull request.
- Add tests for new features.
- Follow the modular structure for new components.

## Community
- Issues and discussions are welcome on GitHub.
- Contributions, feedback, and feature requests encouraged.

## License
MIT License
