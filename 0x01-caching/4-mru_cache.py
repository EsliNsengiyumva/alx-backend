#!/usr/bin/python3
""" Base class for all """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class extends BaseCaching and implements a Most Recently Used caching strategy.
    """

    def __init__(self):
        super().__init__()
        self.order_of_access = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU algorithm)
                mru_key = self.order_of_access.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.order_of_access.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            # Update the order of access
            self.order_of_access.remove(key)
            self.order_of_access.append(key)
            return self.cache_data[key]
        return None
