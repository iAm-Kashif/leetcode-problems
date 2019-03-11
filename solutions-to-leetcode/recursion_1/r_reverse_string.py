"""
Reverse String
https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        s[::] = s[::-1]


def main():
    print(Solution().reverseString(["h", "e", "l", "l", "o"]))

    print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))


if __name__ == "__main__":
    main()
