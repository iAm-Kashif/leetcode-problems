"""
Longest Palindromic Substring
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        if len(s) == 1: return s
        reverse = s[::-1]
        subStrings = []
        sub = ""
        for idx in range(len(s)):
            print(idx, s[idx], reverse[idx])
            if s[idx] == reverse[idx]:
                sub += s[idx]
            elif not s[idx] == reverse[idx]:
                if sub:
                    subStrings.append(sub)
                sub = ""
        return max(subStrings)


def main():
    print(Solution().longestPalindrome("ac"))


if __name__ == "__main__":
    main()
