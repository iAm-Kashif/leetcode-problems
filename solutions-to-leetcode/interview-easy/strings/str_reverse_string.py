"""
Reverse String
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        s[::] = s[::-1]


def main():
    print(Solution().reverseString(["h","e","l","l","o"]))

    print(Solution().reverseString(["H","a","n","n","a","h"]))


if __name__ == "__main__":
    main()
