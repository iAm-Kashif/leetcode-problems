"""
Pascal's Triangle
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution(object):
    out = [[1], [1, 1]]

    def generate(self, numRows: int) -> 'List[List[int]]':
        if not numRows: return []
        if numRows <= 2:
            return self.out[:numRows]
        self.gen(numRows - 2)
        return self.out

    def gen(self, row: int):

        for idx in range(row):
            level = []
            top = self.out[len(self.out) - 1]
            level.append(1)
            for jdx in range(1, len(top)):
                level.append(top[jdx - 1] + top[jdx])
            level.append(1)
            self.out.append(level)


def main():
    print(Solution().generate(3))
    # print(Solution().generate(7))


if __name__ == "__main__":
    main()
