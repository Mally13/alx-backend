#!/urs/bin/env python3
"""
Contains a class BasicCache that inherits from BasicCaching
and is a basic caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
        A caching system class
    """
    def put(self, key, item):
        """Adds an item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value from the cache based on key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
