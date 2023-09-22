#!/usr/bin/env python3
"""Basic dictionary"""

from functools import lru_cache
BaseCaching = __import__("base_caching").BaseCaching


@lru_cache(maxsize=None)
class BasicCache (BaseCaching):
    """Basic dictionary"""

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None