"""
Valid Parentheses
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/302/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isValid(self, s: str) -> bool:
        paren = {")": "(",
                 "}": "{",
                 "]": "["
                 }
        stack = []

        for ch in s:
            if ch in paren.values():
                stack.append(ch)
            else:
                if not stack: return False
                if not stack.pop() == paren[ch]:
                    return False

        return True if not stack else False


def main():
    print(Solution().isValid("{"))


if __name__ == "__main__":
    main()
