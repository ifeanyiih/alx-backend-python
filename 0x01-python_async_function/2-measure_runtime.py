#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time."""


import asyncio
import time
from typing import Callable, List

wait_n: Callable[[int, int], List[float]] = __import__(
                                            '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the time it takes to run wait_n
    Args:
        n (int): n
        max_delay (int): max_delay
    Returns:
        float: The total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    return total/n
