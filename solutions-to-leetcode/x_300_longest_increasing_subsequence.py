"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        longestLengthSub = 0

        for idx in range(len(nums)):
            tmp = [nums[idx]]
            for val in nums[idx + 1:]:
                if val > tmp[-1]:
                    tmp.append(val)
            longestLengthSub = max((len(tmp), longestLengthSub))
        return longestLengthSub


def main():
    # print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 4]))



if __name__ == "__main__":
    main()
