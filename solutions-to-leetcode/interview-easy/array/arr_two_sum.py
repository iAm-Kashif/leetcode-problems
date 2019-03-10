"""
Two Sum
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':

        # complexity: n^2
        # for idx in range(len(nums) - 1):
        #     for jdx in range(idx + 1, len(nums)):
        #         if target == nums[idx] + nums[jdx]:
        #             return [idx, jdx]
        # return []

        # optimization complexity: n
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i


def main():
    print(Solution().twoSum([2, 5, 5, 11], 10))

    print(Solution().twoSum([2, 7, 11, 15], 9))

    print(Solution().twoSum([2, 1, 3, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
