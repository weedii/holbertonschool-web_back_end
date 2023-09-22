#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self):
        """Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            firstKey = next(iter(self.cache_data))
            print(f"DISCARD: {firstKey}")
            self.cache_data.pop(firstKey)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
