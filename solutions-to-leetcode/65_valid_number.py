"""
65. Valid Number
https://leetcode.com/problems/valid-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        index, N = 0, len(s)
        isInteger = False
        if index < N and (s[index] == "+" or s[index] == "-"):
            index += 1
        while index < N and "0" <= s[index] <= "9":
            if not isInteger:
                isInteger = True
            index += 1

        isDecimal = False
        if index < N and s[index] == ".":
            index += 1
            while index < N and "0" <= s[index] <= "9":
                if not isDecimal:
                    isDecimal = True
                index += 1

        isExponent = True
        if index < N and (s[index] == "e" or s[index] == "E"):
            index += 1
            isExponent = False

            if index < N and (s[index] == "+" or s[index] == "-"):
                index += 1
            while index < N and "0" <= s[index] <= "9":
                if not isExponent:
                    isExponent = True
                index += 1

        return (isInteger or isDecimal) and isExponent and index == N

        # Cheat way
        # from decimal import Decimal
        # try:
        #     Decimal(s)
        #     return True
        # except:
        #     return False


def main():
    print(Solution().isNumber(""))

    if __name__ == "__main__":
        main()
