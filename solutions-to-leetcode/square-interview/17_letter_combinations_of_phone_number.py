"""
17. Letter Combinations of a phone number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def letterCombinations(self, digits: str) -> 'List[str]':
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        out = []

        def findCombinations(combination, next_digits):
            if len(next_digits) == 0:
                out.append(combination)
            else:
                for ch in phone[next_digits[0]]:
                    findCombinations(combination + ch, next_digits[1:])

        if digits:
            findCombinations("", digits)
        return out


def main():
    print(Solution().letterCombinations("23"))


if __name__ == "__main__":
    main()
