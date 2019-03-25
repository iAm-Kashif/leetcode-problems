"""
Generate Parentheses
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/discuss/255846/python-Backtrack

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def generateParenthesis(self, n: int) -> 'List[str]':
        res = []

        def bt(left=0, right=0, cur=''):
            print (left, right, cur, res)
            if left == n and right == n:
                res.append(cur)
            if left < n and left >= right:
                bt(left + 1, right, cur + '(')
            if right < n:
                bt(left, right + 1, cur + ')')
            return

        bt()
        return res


def main():
    print(Solution().generateParenthesis(3))


if __name__ == "__main__":
    main()
