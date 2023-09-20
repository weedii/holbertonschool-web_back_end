#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function"""
    start = time.time()
    asyncio.gather(wait_n(n, max_delay))
    end = time.time()
    totalTime = (end-start)
    return totalTime/n
