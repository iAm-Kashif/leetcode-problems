"""
Three Sum
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) < 3: return False
        from itertools import permutations
        sol = dict.fromkeys(tuple(sorted(i)) for i in permutations(nums, 3) if sum(i) == 0)
        return sol.keys()


def main():
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
