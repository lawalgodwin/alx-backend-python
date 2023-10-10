#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yeild 10 rand numbers btw 0 & 10 at an interval of 1sec for each"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
