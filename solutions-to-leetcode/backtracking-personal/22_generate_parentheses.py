"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right - 1)
            if not right:    parens.append(p)
            return parens

        return generate('', n, n)


def main():
    print(Solution().generateParenthesis(3))


if __name__ == "__main__":
    main()
