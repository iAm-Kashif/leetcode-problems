"""
139. Word Break
https://leetcode.com/problems/word-break/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        dp = [False] * len(s)

        for idx in range(len(s)):
            for word in wordDict:
                if word == s[idx - len(word) + 1:idx + 1] and (dp[idx - len(word)] or idx - len(word) == -1):
                    dp[idx] = True
                    break

        return dp[-1]


def main():
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))


if __name__ == "__main__":
    main()
