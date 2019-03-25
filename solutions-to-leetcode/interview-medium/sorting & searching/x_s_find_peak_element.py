"""
Find Peak Element
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def findPeakElement(self, nums: 'List[int]') -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return nums.index(max(nums))
        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] < nums[idx] > nums[idx + 1]:
                return idx
        return None


def main():
    print(Solution().findPeakElement([34, 2]))


if __name__ == "__main__":
    main()
