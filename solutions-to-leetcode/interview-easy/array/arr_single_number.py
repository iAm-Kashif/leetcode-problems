"""
Single Number
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:

        from collections import Counter
        nums = Counter(nums)
        for k, v in nums.items():
            if v == 1:
                return k

        # OR
        # from collections import Counter
        # return Counter(nums).mostcommon()[-1][0]

        # OR using XOR as A XOR A = 0
        # res = 0
        # for item in nums:
        #     res ^= item
        # return res


def main():
    print(Solution().singleNumber([2, 2, 1]))

    print(Solution().singleNumber([4, 1, 2, 1, 2]))


if __name__ == "__main__":
    main()
