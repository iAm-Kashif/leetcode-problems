"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        else: return x == int(str(x)[::-1])


def main():
    pass


if __name__ == "__main__":
    main()
