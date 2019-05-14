"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        dp = [1] + [0] * len(s)
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0

        for idx in range(2, len(s) + 1):
            if 0 < int(s[idx - 1:idx]) <= 9:
                dp[idx] += dp[idx - 1]
            if int(s[idx - 2:idx][0]) != 0 and int(s[idx - 2:idx]) <= 26:
                dp[idx] += dp[idx - 2]
        return dp[len(s)]


def main():
    print(Solution().numDecodings("226"))


if __name__ == "__main__":
    main()

