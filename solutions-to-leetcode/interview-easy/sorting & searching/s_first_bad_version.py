"""
First Bad Version
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return mid


def isBadVersion(n: int):
    pass


def main():
    print(Solution().firstBadVersion(5))


if __name__ == "__main__":
    main()
