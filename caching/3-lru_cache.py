#!/usr/bin/env python3
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache (BaseCaching):
    """LRU Caching"""

    def __init__(self):
        """Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            leastKey = next(iter(self.cache_data))
            print(f"DISCARD: {leastKey}")
            del self.cache_data[leastKey]
        if not key or not item:
            pass

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
