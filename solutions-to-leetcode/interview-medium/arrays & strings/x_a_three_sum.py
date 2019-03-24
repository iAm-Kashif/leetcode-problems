"""
Three Sum
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        out = []
        nums.sort()

        for idx in range(len(nums) - 1):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                if nums[idx] + nums[left] + nums[right] == 0:
                    out.append((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return out
        
        # if len(nums) < 3: return False
        # from itertools import permutations
        # sol = dict.fromkeys(tuple(sorted(i)) for i in permutations(nums, 3) if sum(i) == 0)
        # return sol.keys()


def main():
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
