#!/usr/bin/python3
"""LRU Caching System"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching System"""

    def __init__(self):
        """Initialize LRUCaching"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recently_used = min(self.access_time,
                                      key=self.access_time.get)
            self.cache_data.pop(least_recently_used)
            print("DISCARD: {}".format(least_recently_used))
        self.cache_data[key] = item
        self.access_time[key] = self.access_time_counter
        self.access_time_counter += 1

    def get(self, key):
        """Get the value from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.access_time[key] = self.access_time_counter
        self.access_time_counter += 1
        return self.cache_data[key]
