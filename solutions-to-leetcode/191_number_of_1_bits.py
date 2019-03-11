"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution(object):
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


def main():
    print(Solution().hammingWeight(11))
    print(Solution().hammingWeight(128))


if __name__ == "__main__":
    main()
