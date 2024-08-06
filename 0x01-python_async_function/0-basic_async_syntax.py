#!/usr/bin/env python3
"""code to use async and await"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        function to await between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
