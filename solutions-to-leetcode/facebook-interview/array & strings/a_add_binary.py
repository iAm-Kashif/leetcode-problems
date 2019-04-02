"""
Add Binary
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/263/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    print(Solution().addBinary("1010", "1011"))


if __name__ == "__main__":
    main()
