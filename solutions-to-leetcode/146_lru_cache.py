"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

_author:            Kashif Memon
_python_version:    3.7.2
"""

from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        print('g', self)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        print('p1', self)
        if len(self) > self.capacity:
            self.popitem(last=False)
            print('p2', self)


def main():
    c = LRUCache(capacity=2)
    c.put(1, 1)
    c.put(2, 2)
    c.get(1)
    c.put(3, 3)
    c.get(2)
    c.put(4, 4)
    c.get(1)
    c.get(3)
    c.get(4)


if __name__ == "__main__":
    main()
