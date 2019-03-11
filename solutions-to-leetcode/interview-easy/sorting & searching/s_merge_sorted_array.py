"""
Merge Sorted Array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        nums1[::] = nums1[:m] + nums2[:n]
        nums1[::] = sorted(nums1)


def main():
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


if __name__ == "__main__":
    main()
