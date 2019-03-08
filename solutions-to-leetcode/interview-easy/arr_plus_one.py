"""
Plus One
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        num = int("".join(str(x) for x in digits)) + 1
        return [int(x) for x in str(num)]


def main():
    print(Solution().plusOne([9]))

    print(Solution().plusOne([1, 2, 3]))

    print(Solution().plusOne([4, 3, 2, 1]))


if __name__ == "__main__":
    main()
