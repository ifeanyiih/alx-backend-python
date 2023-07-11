#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself."""
import asyncio
import time
from typing import Callable, List
async_comprehension: Callable[[], List[float]] = __import__(
                                '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total run time of running four
    async_comprehension coroutines concurrently"""
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total = time.perf_counter() - start
    return total
