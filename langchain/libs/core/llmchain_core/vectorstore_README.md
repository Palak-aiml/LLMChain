# Vector Store and Embeddings

## Vector Store

The vector store provides a simple interface for storing and searching vectors with optional metadata. The base class `VectorStore` defines the interface, and `SimpleVectorStore` is an in-memory implementation using cosine similarity for search.

## Embeddings

The embeddings interface allows you to convert text into vectors. The base class `Embeddings` defines the interface, and `SimpleEmbedding` provides a trivial implementation using character ordinals.

## Retriever with Embeddings

`RetrieverWithEmbeddings` combines an embedding model and a vector store to enable semantic search over documents.

### Example Usage

```python
from llmchain_core.simple_embedding import SimpleEmbedding
from llmchain_core.simple_vectorstore import SimpleVectorStore
from llmchain_core.retriever_with_embeddings import RetrieverWithEmbeddings

embedding = SimpleEmbedding()
vector_store = SimpleVectorStore()
retriever = RetrieverWithEmbeddings(embedding, vector_store)

retriever.add_document("hello world", metadata="doc1")
retriever.add_document("goodbye world", metadata="doc2")
results = retriever.retrieve("hello")
print(results)  # Should include 'doc1'
```
