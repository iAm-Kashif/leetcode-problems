"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def findMedianSortedArrays(nums1: 'List[int]', nums2: 'List[int]') -> 'float':
    sorted_joined = sorted(nums1 + nums2)
    print(sorted_joined)
    if len(sorted_joined) % 2 == 0:
        index = int(len(sorted_joined) / 2)
        return (sorted_joined[index] + sorted_joined[index-1])/2
    else:
        index = (int(len(sorted_joined)/2))
        return sorted_joined[index]


def main():
    nums11 = [1, 3]
    nums12 = [2]
    # print("The median is", findMedianSortedArrays(nums11, nums12))

    nums21 = [1, 2]
    nums22 = [3, 4]
    print("The median is", findMedianSortedArrays(nums21, nums22))


if __name__ == "__main__":
    main()