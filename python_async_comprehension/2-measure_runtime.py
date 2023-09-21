#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime function"""
    start = time.time()
    for i in range(4):
        await asyncio.gather(async_comprehension())
    end = time.time()
    totalTime = end-start
    finalTime = totalTime/4
    return finalTime
