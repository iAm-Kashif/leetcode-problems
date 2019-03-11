"""
Reverse Bits
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution(object):
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[::-1][:-2] + '0'*(34 - len(bin(n))), 2)


def main():
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits(128))


if __name__ == "__main__":
    main()
