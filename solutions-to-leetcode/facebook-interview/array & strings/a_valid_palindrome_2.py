"""
Valid Palindrome II
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/288/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(start, end):
            newS = s[start:end + 1]
            return newS == newS[::-1]
            # while start < end:
            #     if not s[start] == s[end]:
            #         return False
            #     start += 1
            #     end -= 1
            # else:
            #     return True

        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start] == s[end]:
                return isPalindrome(start + 1, end) or isPalindrome(start, end - 1)
            start += 1
            end -= 1
        else:
            return True


def main():
    print(Solution().validPalindrome(s="abc"))


if __name__ == "__main__":
    main()
