"""
Permutations
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        # out = []
        # from itertools import permutations
        # for item in permutations(nums, len(nums)):
        #     out.append(list(item))
        # return out

        # Using Recursion
        if not list: return []
        if len(nums) == 1: return [nums]
        out = []
        for idx in range(len(nums)):
            val = nums[idx]

            remList = nums[:idx] + nums[idx + 1:]
            for item in self.permute(remList):
                out.append([val] + item)
        return out


def main():
    print(Solution().permute([1, 2, 3]))


if __name__ == "__main__":
    main()
