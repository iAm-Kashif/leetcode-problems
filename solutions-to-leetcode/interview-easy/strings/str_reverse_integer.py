"""
Reverse Integer
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def reverse(self, x: int) -> None:
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = str(x)[1:]
            x = int("-" + x[::-1])
        return x


def main():
    print(Solution().reverse(123))

    print(Solution().reverse(-123))

    print(Solution().reverse(120))


if __name__ == "__main__":
    main()
