"""
Scaling: Utilities for async execution and batching to support high-throughput workloads.
"""
import asyncio
from concurrent.futures import ThreadPoolExecutor

def run_async(func):
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper

def batch_process(items, batch_size, process_fn):
    for i in range(0, len(items), batch_size):
        yield process_fn(items[i:i+batch_size])
