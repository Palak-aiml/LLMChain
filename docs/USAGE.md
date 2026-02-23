# LLMChain Usage Guide

## Installation
```bash
pip install -r requirements.txt
```

## Quick Start
See the `templates/` directory for ready-to-use examples:
- QA chain
- Summarization chain
- Conversational chain

## Running the UI
```bash
pip install fastapi uvicorn
uvicorn ui.app:app --reload
```

## Experiment Tracking
See `llmchain/monitoring/experiment/experiment_tracker.py` for logging runs, metrics, and artifacts.

## Advanced Features
- Distributed tracing: `llmchain/enterprise/distributed_tracing.py`
- Security: `llmchain/enterprise/security.py`
- Scaling: `llmchain/enterprise/scaling.py`

## More
- See API_REFERENCE.md for full API details.
- See TUTORIALS.md for step-by-step guides.
