#!/usr/bin/env python3
""" LIFO caching"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = sorted(self.cache_data)[-1]
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
