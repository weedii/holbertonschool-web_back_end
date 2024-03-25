#!/usr/bin/env python3
import redis
import uuid
from typing import Union

"""
Cache Class
"""


class Cache():
    """Cache Class"""

    def __init__(self):
        """__init__ method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method generate random key
        and store data in it in the redis db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
