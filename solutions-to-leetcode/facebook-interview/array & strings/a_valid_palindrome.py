"""
Valid Palindrome
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/288/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        import re
        s = re.sub(r"[^a-zA-Z0-9]*", "", s).lower()
        return s == s[::-1]

        # for idx in range(len(s) // 2):
        #     if not s[idx] == s[-(idx + 1)]:
        #         return False
        # else:
        #     return True

        s = "".join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]


def main():
    print(Solution().isPalindrome(s="ab_a"))


if __name__ == "__main__":
    main()
