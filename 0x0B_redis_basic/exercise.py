#!/usr/bin/env python3
from tkinter import N
import redis
import uuid
from typing import Union, Callable

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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """will return converted data back to the desired format"""
        data = self._redis.get(key)
        if data is None:
            return None
        else:
            if fn is None:
                return data
            else:
                return fn(data)

    def get_str(self, key: str) -> str:
        """will automatically parametrize Cache.get"""
        self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """will automatically parametrize Cache.get"""
        self.get(key, fn=int)
