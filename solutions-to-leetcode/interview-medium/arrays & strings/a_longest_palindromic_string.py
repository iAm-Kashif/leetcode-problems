"""
Valid Sodoku
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromeSubstrings = []
        rev_s = s[::-1]
        loopSubstring = ""

        for idx in range(len(s)):
            if s[idx] == rev_s[idx]:
                loopSubstring += s[idx]
            elif not s[idx] == rev_s[idx]:
                if len(loopSubstring):
                    palindromeSubstrings.append(loopSubstring)
                    loopSubstring = ""
        if loopSubstring:
            palindromeSubstrings.append(loopSubstring)
        if palindromeSubstrings:
            return max(palindromeSubstrings, key=len)
        return ""



def main():
    print(Solution().longestPalindrome("acca"))

    # print(Solution().longestPalindrome("babad"))
    #
    # print(Solution().longestPalindrome("cbbd"))


if __name__ == "__main__":
    main()
