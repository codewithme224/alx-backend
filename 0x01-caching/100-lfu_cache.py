#!/usr/bin/python3
"""LFU Caching System"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class `LFUCache` that inherits from
       `BaseCaching`
    """

    def __init__(self):
        """initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = [item, 0]
        else:
            self.cache_data[key][0] = item
        self.cache_data.move_to_end(key, last=False)
        self.cache_data[key][1] += 1

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data[key][1] += 1
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, [None])[0]
