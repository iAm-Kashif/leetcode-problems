"""
Numeric Palindromes

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def is_numeric_palindrome(self, n: int) -> bool:
        rev_n = int(str(n)[::-1])
        return n == rev_n


def main():
    print(Solution().is_numeric_palindrome(123))


if __name__ == "__main__":
    main()
