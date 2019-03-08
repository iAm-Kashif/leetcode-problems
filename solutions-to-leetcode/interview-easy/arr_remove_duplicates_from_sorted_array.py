"""
Remove Duplicates from Sorted Array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


def main():
    print(Solution().removeDuplicates([1, 1, 1, 1]))

    print(Solution().removeDuplicates([1, 1, 2]))

    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    main()
