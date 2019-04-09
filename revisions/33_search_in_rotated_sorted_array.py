class Solution:
    def search(self, nums: 'List[int]', target: int):

        def get_pivot(start, end):
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

        def binary_search(start, end):
            while start <= end:
                mid = (start + end) // 2

                if target == nums[mid]:
                    return mid
                else:
                    if target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1

        if not nums:
            return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1

        pivot = get_pivot(0, len(nums) - 1)

        if pivot == 0:
            return binary_search(0, len(nums) - 1)
        else:
            if target < nums[0]:
                return binary_search(pivot, len(nums) - 1)
            else:
                return binary_search(0, pivot)


print(Solution().search([4, 5, 6, 0, 1, 2, 3], 3))
