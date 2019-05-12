"""
401. Binary Watch
https://leetcode.com/problems/binary-watch/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def readBinaryWatch(self, num: int) -> 'List[str]':
        return [
            "%d:%02d" % (hour, minute)
            for hour in range(12) for minute in range(60)
            if (bin(hour) + bin(minute)).count("1") == num
        ]


def main():
    print(Solution().readBinaryWatch(1))


if __name__ == "__main__":
    main()
