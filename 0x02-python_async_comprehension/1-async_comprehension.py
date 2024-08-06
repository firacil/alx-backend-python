#!/usr/bin/env python3
"""import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no argument

coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return 10 random numbers
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
