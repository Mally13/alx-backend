#!/urs/bin/env python3
"""
Contains a class MRUCache that inherits from BasicCaching
and is a MRU caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines:
        A MRU caching system class
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data_order = []

    def put(self, key, item):
        """Adds an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                if key in self.cache_data_order:
                    self.cache_data_order.remove(key)
                    self.cache_data.pop(key)
                else:
                    key_pop = self.cache_data_order.pop(-1)
                    self.cache_data.pop(key_pop)
                    print(f'DISCARD: {key_pop}')
            self.cache_data[key] = item
            self.cache_data_order.append(key)

    def get(self, key):
        """Gets the value from the cache based on key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        key_to_shift = self.cache_data_order.remove(key)
        self.cache_data_order.append(key)
        return self.cache_data.get(key)
