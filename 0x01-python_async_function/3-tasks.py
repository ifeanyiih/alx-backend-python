#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function, use the
regular function syntax to do this) task_wait_random that
takes an integer max_delay and returns a asyncio.Task."""
import asyncio
from typing import Callable

wait_random: Callable[[int], float] = __import__(
                                    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task type
    Args:
        max_delay (int): max_delay
    Returns:
        asyncio.Task: an asyncio.Task type
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
