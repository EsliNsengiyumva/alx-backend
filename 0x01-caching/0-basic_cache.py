#!/usr/bin/python3

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class extends BaseCaching and implements a simple caching strategy.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
