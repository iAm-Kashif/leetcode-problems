"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

_author:            Kashif Memon
_python_version:    3.7.2
"""
from collections import OrderedDict


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# This idea uses a dictionary with doubly LinkedList to work with O(1) complexity
# dic stores {key, node}
# Idea is; any new kv added, is added at start of LL. so oldest items (removable) is behind tail always
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}  # [0]
        self.head = Node(0, 0)  # [3]
        self.tail = Node(0, 0)  # [3]
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def promote(self, node):  # [1]
        # set the node next to head
        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.promote(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.promote(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:  # [2]
            del self.dic[self.tail.prev.key]
            self.remove(self.tail.prev)


# The idea here is to use an orderedDict where
# new items are always added at end of list (as normally).
# any fetch request would move items to end of list, making start of list removable for newer items if necessary

class LRUCache_dict:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


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
