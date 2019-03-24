"""
Digit Sum

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def digit_sum(self, number: int) -> int:
        sum = 0
        for ch in str(number):
            if ch.isdigit():
                sum += int(ch)
        return sum


def main():
    print(Solution().digit_sum(-3456))


if __name__ == "__main__":
    main()
