"""
Minimum Size Subarray Sum
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/328/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: 'List[int]') -> int:
        total = 0
        left = 0
        minLen = float("inf")

        for right, val in enumerate(nums):
            total += val

            while total >= s:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if minLen == float("inf") else minLen


def main():
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))


if __name__ == "__main__":
    main()
