"""
Valid Palindrome
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r"\W","",s).lower()

        for idx in range(len(s)//2):
            if not s[idx] == s[-(idx+1)]:
                return False
        return True

        # OR
        # s = re.sub(r"\W+", "", s).lower()
        # return s == s[::-1]




def main():
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

    print(Solution().isPalindrome("race a car"))


if __name__ == "__main__":
    main()
