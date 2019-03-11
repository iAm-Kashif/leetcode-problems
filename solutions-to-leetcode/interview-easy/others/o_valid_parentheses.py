"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isValid(self, s: str) -> bool:

        charHashMap = {")": "(", "}": "{", "]": "["}
        stack = []

        if len(s) % 2 != 0:
            return False
        for item in s:
            if item in charHashMap.values():
                stack.append(item)

            if item in charHashMap.keys():
                if not stack:
                    return False
                topElement = stack.pop()
                if not topElement == charHashMap[item]:
                    return False

        if not stack:
            return True
        return False


def main():
    # print(Solution().isValid(s="()"))
    #
    # print(Solution().isValid(s="()[]{}"))
    #
    # print(Solution().isValid(s="(]"))
    #
    # print(Solution().isValid(s="([)]"))
    #
    # print(Solution().isValid(s="{[]}"))

    print(Solution().isValid(s="){"))


if __name__ == "__main__":
    main()
