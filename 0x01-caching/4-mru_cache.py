#!/usr/bin/python3
""" MRU Caching System """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A class MRUCache that inherits from BaseCaching """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(mru_key)
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
