#!/usr/bin/python3
"""Base caching implementation"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class extends BaseCaching and implements a First-In-First-Out caching strategy.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the first item (FIFO algorithm)
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

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
