"""
Three Sum
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return []
        out = []
        nums.sort()

        for idx in range(len(nums) - 2):
            # sorted array and now all are positive numbers; sum can never be 0
            if nums[idx] > 0: break
            # if the same number again, we've checked it, so ignore.
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

        # if len(nums) < 3: return False
        # from itertools import permutations
        # sol = dict.fromkeys(tuple(sorted(i)) for i in permutations(nums, 3) if sum(i) == 0)
        # return sol.keys()


def main():
    # print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-2, 0, 0, 2, 2]))


if __name__ == "__main__":
    main()
