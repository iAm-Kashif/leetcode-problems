"""
Pascal's Triangle 2
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1660/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def getRow(self, rowIndex: int) -> 'List[int]':
        # if not rowIndex: return []
        # out = []
        #
        # for idx in range(rowIndex):
        #     row = [None for _ in range(idx + 1)]
        #     row[0] = row[-1] = 1
        #
        #     for jdx in range(1, len(row) - 1):
        #         row[jdx] = out[idx - 1][jdx - 1] + out[idx - 1][jdx]
        #     out.append(row)
        # return out[rowIndex-1]

        if rowIndex == 0: return [1]
        ans = self.getRow(rowIndex - 1)
        print(ans)
        return [1] + [sum(x) for x in zip(ans, ans[1:])] + [1]


def main():
    print(Solution().getRow(rowIndex=5))


if __name__ == "__main__":
    main()
