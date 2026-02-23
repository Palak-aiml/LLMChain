"""
MapReduceChain: Composable chain for map-reduce style document processing.
"""
from typing import List, Callable

class MapReduceChain:
    def __init__(self, map_chain: Callable, reduce_chain: Callable):
        self.map_chain = map_chain
        self.reduce_chain = reduce_chain

    def run(self, documents: List[str], **kwargs):
        mapped = [self.map_chain(doc, **kwargs) for doc in documents]
        return self.reduce_chain(mapped, **kwargs)
