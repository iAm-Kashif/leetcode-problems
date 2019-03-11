"""
Missing Number
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def missingNumber(self, nums: 'List[int]') -> int:
        for idx in range(len(nums)+1):
            if idx not in nums:
                return idx

        # return len(nums) * (len(nums) + 1) / 2 - sum(nums)


def main():
    print(Solution().missingNumber([0]))
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()
