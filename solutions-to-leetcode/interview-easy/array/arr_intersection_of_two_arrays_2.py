"""
Intersection of Two Arrays II
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        from collections import Counter
        nums1, nums2 = map(Counter, (nums1, nums2))
        return list((nums1 & nums2).elements())

        # Wrong as making a set removed duplicate values
        # return list(set(nums1) & set(nums2))
        # return set(nums1).intersection(nums2)

        # Not working for Case-1 as nums2=[2] and result=[2,2] but needs to be just [2]
        # return [value for value in nums1 if value in nums2]


def main():
    print(Solution().intersect([1, 2, 2, 1], [2,2]))

    # print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))


if __name__ == "__main__":
    main()
