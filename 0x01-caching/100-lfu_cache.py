#!/usr/bin/python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Implementation of LFU (Least Frequently Used) caching algorithm with LRU tie-breaking.
    """

    def __init__(self):
        super().__init__()
        self.frequency_counter = {}

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key exists, update the frequency
                self.frequency_counter[key] += 1
            else:
                # If the key is new, set frequency to 1
                self.frequency_counter[key] = 1

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequency used item (LFU algorithm)
                least_frequent_keys = [k for k, v in self.frequency_counter.items() if v == min(self.frequency_counter.values())]
                if len(least_frequent_keys) > 1:
                    # Use LRU algorithm to break the tie
                    lfu_key = min(least_frequent_keys, key=lambda k: self.cache_data[k]['timestamp'])
                else:
                    lfu_key = least_frequent_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency_counter[lfu_key]
                print("DISCARD:", lfu_key)

            # Update the cache with the new item
            self.cache_data[key] = {'value': item, 'timestamp': self.timestamp}
            self.timestamp += 1

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            # Update the frequency and timestamp
            self.frequency_counter[key] += 1
            self.cache_data[key]['timestamp'] = self.timestamp
            return self.cache_data[key]['value']
        return None
