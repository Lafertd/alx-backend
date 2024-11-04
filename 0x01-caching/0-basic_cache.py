#!/usr/bin/python3
"""
BasicCache module
"""

BasicCache = __import__('base_caching').BaseCaching

class BasicCache(BasicCache):
    """
    BasicCache class that inherits from BaseCaching and implements
    a basic caching system.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item if found, or None if the key is not in the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key)  # Return the value for the specified key
