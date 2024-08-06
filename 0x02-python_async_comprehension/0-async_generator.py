#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
