"""
65. Valid Number
https://leetcode.com/problems/valid-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip() + " "
        idx = 0
        dot, digit = 0, 0

        if s[idx] == "+" or s[idx] == "-":
            idx += 1
        while s[idx].isdigit() or s[idx] == ".":
            if s[idx] == ".":
                dot += 1
            if s[idx].isdigit():
                digit += 1
            idx += 1
        if dot > 1 or digit <= 0: return False

        if s[idx] == "e":
            if s[idx + 1] == "+" or s[idx + 1] == "-":
                idx += 1
            sright = s[idx + 1:]
            if not sright.strip().isdigit():
                return False
            idx += len(sright)
        return len(s) - 1 == idx


def main():
    print(Solution().isNumber("0"))

    if __name__ == "__main__":
        main()
