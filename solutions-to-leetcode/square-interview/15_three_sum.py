"""
15. Three Sum
https://leetcode.com/problems/3sum/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return []
        out = []
        nums.sort()

        for idx in range(len(nums) - 2):

            if nums[idx] > 0: break
            if idx > 0 and nums[idx] == nums[idx - 1]: continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[idx] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    if (nums[idx], nums[left], nums[right]) not in out:
                        out.append((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return out


def main():
    # print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-2, 0, 0, 2, 2]))


if __name__ == "__main__":
    main()
