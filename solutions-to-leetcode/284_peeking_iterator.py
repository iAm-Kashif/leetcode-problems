"""
284. Peeking Iterator
https://leetcode.com/problems/peeking-iterator/

_author:            Kashif Memon
_python_version:    3.7.2
"""


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums: 'List[int]'):
        """
        Initializes an iterator object to the beginning of a list.
        """

    def hasNext(self) -> bool:
        """
        Returns true if the iteration has more elements.
        """

    def next(self) -> int:
        """
        Returns the next element in the iteration.
        """


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        """
        self.iter = iterator
        self.data = self.iter.next() if self.iter.hasNext() else None

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        return self.data

    def next(self) -> int:
        data = self.data
        self.data = self.iter.next() if self.iter.hasNext() else None
        return data

    def hasNext(self) -> bool:
        return self.data is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
