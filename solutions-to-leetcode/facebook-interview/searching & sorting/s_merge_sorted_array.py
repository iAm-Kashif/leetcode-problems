"""
Merge Sorted Array
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/309/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[::] = nums1[:m] + nums2[:n]
        nums1[::] = sorted(nums1)


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    print(Solution().merge(nums1, 3, nums2, 3))


if __name__ == "__main__":
    main()
