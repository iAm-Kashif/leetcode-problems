"""
Shuffle Array

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution(object):

    def __init__(self, nums: 'List[int]'):
        self._array = nums

    def reset(self) -> 'List[int]':
        return self._array

    def shuffle(self) -> 'List[int]':
        import random
        shuffled_array = self._array[:]
        random.shuffle(shuffled_array)
        return shuffled_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
