"""
78. Subsets
https://leetcode.com/problems/subsets/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        # out = []
        # from itertools import combinations
        # for idx in range(len(nums) + 1):
        #     for item in combinations(nums, idx):
        #         out.append(list(item))
        # return out

        # Using Recursion
        if not nums: return [[]]
        res_subsets = self.subsets(nums[1:])
        return res_subsets + [[nums[0]] + i for i in res_subsets]


def main():
    print(Solution().subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
