"""
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def search(self, nums: 'List[int]', target: int) -> bool:
        start = 0
        end = len(nums) - 1
        pass


def main():
    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))

    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3))


if __name__ == "__main__":
    main()
