"""
46. Permutations
https://leetcode.com/problems/permutations/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return []
        if len(nums) == 1: return [nums]

        out = []
        for idx in range(len(nums)):
            val = nums[idx]

            rem = nums[:idx] + nums[idx + 1:]
            for item in self.permute(rem):
                out.append([val] + item)
        return out


def main():
    print(Solution().permute([1, 2, 3]))


if __name__ == "__main__":
    main()
