"""
Subsets
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

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
        out = []
        self.sub(nums, 0, [], out)
        return out

    def sub(self, nums, index, path, out):
        out.append(path)
        for idx in range(index, len(nums)):
            print("idx", idx, "Calling", idx + 1,"path", path, "newP", path + [nums[idx]], "o:", out)
            self.sub(nums, idx+1, path + [nums[idx]], out)


def main():
    print(Solution().subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
