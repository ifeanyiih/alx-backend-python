#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called."""
import asyncio
from typing import Callable, List

task_wait_random: Callable[[int], asyncio.Task] = __import__(
                                            '3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call wait_random n times and return list with float values
    Args:
        n (int): number of calls
        max_delay (int): max_delay
    Returns:
        list: a list of float values
    """
    rands = sorted(await asyncio.gather(*(task_wait_random(max_delay)
                   for i in range(n))))
    return rands
