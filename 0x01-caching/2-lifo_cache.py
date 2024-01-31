#!/usr/bin/python3

"""Keyword arguments:argument -- description
Return: return_description
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class extends BaseCaching and implements a Last-In-First-Out caching strategy.
    """

    def __init__(self):
        """
        Initialize an instance of LIFOCache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            # Assign the item value for the key
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the last item put in the cache (LIFO algorithm)
                last_item_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_item_key]
                print("DISCARD:", last_item_key)

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
