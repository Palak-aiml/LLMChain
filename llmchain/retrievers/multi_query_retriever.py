"""
MultiQueryRetriever: Retrieves documents using multiple queries and merges results.
"""
from typing import List, Callable

class MultiQueryRetriever:
    def __init__(self, retriever, query_generators: List[Callable[[str], str]]):
        self.retriever = retriever
        self.query_generators = query_generators

    def retrieve(self, query: str) -> List[str]:
        all_results = []
        for gen in self.query_generators:
            q = gen(query)
            results = self.retriever.retrieve(q)
            all_results.extend(results)
        # Optionally deduplicate
        return list(set(all_results))
