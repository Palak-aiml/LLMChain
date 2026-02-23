# RetrieverWithCallbacks

A retriever wrapper that supports post-retrieval callbacks for logging, monitoring, or custom hooks.

## Usage
```python
from llmchain.core.retriever_with_callbacks import RetrieverWithCallbacks

# Example retriever (must have a .retrieve(query) method)
class DummyRetriever:
    def retrieve(self, query):
        return [f"Result for {query}"]

def log_callback(query, results):
    print(f"Query: {query}, Results: {results}")

retriever = DummyRetriever()
cb_retriever = RetrieverWithCallbacks(retriever, callbacks=[log_callback])
results = cb_retriever.retrieve("What is LLMChain?")
```
