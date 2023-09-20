#!/usr/bin/env python3
"""Async Comprehensions"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async_comprehension function"""
    randomNumbers = []
    async for i in async_generator():
        randomNumbers.append(i)
    return randomNumbers
