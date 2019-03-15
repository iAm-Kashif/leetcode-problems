"""
17. Letter Combinations of a phone number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    out = []

    def letterCombinations(self, digits: str) -> 'List[str]':
        if digits:
            from itertools import permutations
            # permList = list(permutations(digits))
            # for idx in range(len(permList)):
            #     permList[idx] = "".join(permList[idx])
            # print(permList)
            # self.findCombinations("", permList[idx])
            self.findCombinations("", digits)
        return self.out

    def findCombinations(self, combine: str, digits: str) -> 'List':
        # print(">start", combine, digits)
        if len(digits) == 0:
            self.out.append(combine)
        else:
            # print(">mid", digits[0], self.phone[digits[0]])
            for charLetter in self.phone[digits[0]]:
                # print(">end", combine + charLetter, digits[1:])
                self.findCombinations(combine + charLetter, digits[1:])


def main():
    print(Solution().letterCombinations("234"))


if __name__ == "__main__":
    main()
