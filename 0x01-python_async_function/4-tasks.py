#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a
new function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async"""
    # create a list of the coroutines
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # return a list of the ruturns of each coroutines in the order they are
    # completed
    return [await task for task in asyncio.as_completed(tasks)]
