"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        mGlobal = mLocal = nums[0]

        for idx in range(1, len(nums)):
            mLocal = max(mLocal + nums[idx], nums[idx])
            mGlobal = max(mLocal, mGlobal)
        return mGlobal


def main():
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
