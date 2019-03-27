"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        if not nums: return -1
        if len(nums) == 1: return 0 if target in nums else -1

        pivot = self.get_pivot(0, len(nums) - 1, nums)

        if target == nums[pivot]:
            return pivot

        if pivot == 0:
            return self.b_search(0, len(nums) - 1, nums, target)
        if target < nums[0]:
            return self.b_search(pivot, len(nums) - 1, nums, target)
        else:
            return self.b_search(0, pivot - 1, nums, target)

    def b_search(self, start, end, nums, target):
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def get_pivot(self, start, end, nums):
        if nums[start] < nums[end]:
            return 0

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1


def main():
    print(Solution().search([6, 7, 1, 2, 3, 4, 5], 6))


if __name__ == "__main__":
    main()
