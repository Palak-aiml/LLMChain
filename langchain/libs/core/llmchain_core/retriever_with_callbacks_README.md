# Retriever With Callbacks

## Overview

`RetrieverWithCallbacks` extends the retriever to support callback functions that are invoked after each retrieval. This allows for logging, monitoring, or custom post-processing of retrieval results.

## Usage Example

```python
from llmchain_core.simple_embedding import SimpleEmbedding
from llmchain_core.simple_vectorstore import SimpleVectorStore
from llmchain_core.retriever_with_callbacks import RetrieverWithCallbacks

def my_callback(query, results):
    print(f"Query: {query}, Results: {results}")

embedding = SimpleEmbedding()
vector_store = SimpleVectorStore()
retriever = RetrieverWithCallbacks(embedding, vector_store, on_retrieve=my_callback)

retriever.add_document("foo bar", metadata="doc1")
retriever.retrieve("foo")
```

The callback receives the query and the list of results.
