"""
Search in Rotated Sorted Array II
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/284/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        if not nums: return False
        if len(nums) == 1: return True if target == nums[0] else False

        pivot = self.get_pivot(0, len(nums) - 1, nums)

        if target == nums[pivot]:
            return True

        if pivot == 0:
            return self.b_search(0, len(nums) - 1, nums, target)
        if target < nums[0]:
            return self.b_search(pivot + 1, len(nums) - 1, nums, target)
        else:
            return self.b_search(0, pivot - 1, nums, target)

    def b_search(self, start, end, nums, target):
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False

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
    # [2, 5, 6, 0, 0, 1, 2]
    print(Solution().search([5, 5], 11))


if __name__ == "__main__":
    main()
