"""
Maximum Size Subarray Sum Equals k
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/297/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
        hashMap = {0: -1}
        total = 0
        maxLen = 0

        for idx in range(len(nums)):
            total += nums[idx]

            if total not in hashMap:
                hashMap[total] = idx

            if total - k in hashMap:
                maxLen = max(maxLen, idx - hashMap[total - k])
        return maxLen


def main():
    # print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))  # 4

    print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))  # 2


if __name__ == "__main__":
    main()
