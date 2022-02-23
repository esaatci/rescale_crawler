from collections import OrderedDict


class LRUCache:
    """
    A basic LRU cache for keeping track of the visited urls
    It's interface is specifically for the crawler so it doesn't have
    methods like remove or update.

    Instead of storing the urls we could have stored
    their hashes to reduce the memory overhead.

    LRU policy seems like a good option for the eviction policy because
    If we the evicted url is the least recently used, then it's very likely we will not
    encounter it in the future.

    However, the above is an assumption and its hard to say what policy will work the best
    without doing some analysis on how the graph topology looks like.
    """

    def __init__(self, maximum_size):
        self.__cache = OrderedDict()
        self.__maximum_size = maximum_size

    def has(self, key):
        if key not in self.__cache:
            return False
        self.__mark_used(key)
        return True

    def insert(self, key):
        if key in self.__cache:  # more of a defensive check
            return

        self.__cache[key] = 1
        self.__mark_used(key)

        if len(self.__cache) > self.__maximum_size:
            self.__cache.popitem(last=False)

    def __mark_used(self, key):
        self.__cache.move_to_end(key)
