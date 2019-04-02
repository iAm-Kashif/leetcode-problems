"""
Intersection of Two Arrays 2
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/270/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        from collections import Counter
        nums1, nums2 = map(Counter, (nums1, nums2))
        return list((nums1 & nums2).elements())


def main():
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))


if __name__ == "__main__":
    main()
