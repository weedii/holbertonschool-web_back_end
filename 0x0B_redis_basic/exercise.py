#!/usr/bin/env python3
import redis
import uuid
from typing import Union

"""
Cach Class
"""


class Cache():

    def __init__(self):
        """__init__ method"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data):
        """store method generate random key and store data in it"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
