#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1
second, then yield a random number between 0 and 10. Use the random module."""
import asyncio
from typing import Iterator
import random


async def async_generator() -> Iterator:
    """A async generator function that takes no arg
    It yields the values
    """
    for i in range(10):
        number: float = random.uniform(0, 10)
        yield number
        await asyncio.sleep(1)
