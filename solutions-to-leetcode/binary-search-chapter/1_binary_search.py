"""
Binary Search
https://leetcode.com/explore/learn/card/binary-search/138/background/1038/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def binarySearch(nums: 'List[int]', target: 'int') -> 'int':
    mid = int (len(nums) / 2)
    for index in range(mid):
        if target > nums[mid]


def main():
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    binarySearch(nums1, target1)

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    # binarySearch(nums2, target2)


if __name__ == "__main__":
    main()