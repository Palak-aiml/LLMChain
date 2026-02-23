# LLMChain Tutorials

## 1. Building a QA Chain
- See `templates/qa_chain_template.py` for a full example.
- Customize the retriever, LLM, and prompt manager as needed.

## 2. Summarization Chain
- See `templates/summarization_chain_template.py`.
- Pass your documents to the chain and get a summary.

## 3. Conversational Chain
- See `templates/conversational_chain_template.py`.
- Use `ChatMemory` for multi-turn conversations.

## 4. Experiment Tracking
- Use `ExperimentTracker` to log runs, metrics, and artifacts.
- Example:
  ```python
  from llmchain.monitoring.experiment.experiment_tracker import ExperimentTracker
  tracker = ExperimentTracker()
  run_id = tracker.start_run(run_name="myrun", params={"lr":0.01})
  tracker.log_metric("accuracy", 0.95)
  tracker.end_run()
  ```

## 5. Using the UI
- Run `uvicorn ui.app:app --reload` and open http://localhost:8000
- Use the visual builder and dashboard.

## 6. Plugins
- Add plugins to extend LLMChain with new tools, retrievers, or chains.

---
For more, see the README and API_REFERENCE.md.
