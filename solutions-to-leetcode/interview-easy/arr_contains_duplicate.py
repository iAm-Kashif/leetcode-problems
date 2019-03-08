"""
Contains Duplicate
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

        # return len(nums) != len(set(nums))


def main():
    print(Solution().containsDuplicate([1, 2, 3, 1]))

    print(Solution().containsDuplicate([1, 2, 3, 4]))

    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    main()
