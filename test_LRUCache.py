import unittest
from LRUCache import LRUCache


class LRUCacheTests(unittest.TestCase):
    def test_returns_false_when_key_not_in_cache(self):
        cache = LRUCache(1)
        key = "link.com"
        self.assertFalse(cache.has(key))

    def test_inserts_key(self):
        cache = LRUCache(1)
        key = "link.com"
        cache.insert(key)
        self.assertTrue(cache.has(key))

    def test_evicts_least_recently_used_key(self):
        cache = LRUCache(3)
        key1 = "link1"
        key2 = "link2"
        key3 = "link3"
        key4 = "link4"

        cache.insert(key1)
        cache.insert(key2)
        cache.insert(key3)
        cache.insert(key4)

        self.assertFalse(cache.has(key1))

        self.assertTrue(cache.has(key2))
        self.assertTrue(cache.has(key3))
        self.assertTrue(cache.has(key4))

    def test_updates_existing_keys_lru_when_searched(self):
        cache = LRUCache(3)
        key1 = "link1"
        key2 = "link2"
        key3 = "link3"

        cache.insert(key1)
        cache.insert(key2)
        cache.insert(key3)

        cache.has(key1)

        key4 = "link4"
        cache.insert(key4)

        self.assertFalse(cache.has(key2))
        self.assertTrue(cache.has(key1))
