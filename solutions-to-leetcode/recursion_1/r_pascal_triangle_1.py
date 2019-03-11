"""
Pascal's Triangle 1
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1659/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def generate(self, num_rows: int) -> 'List[List[int]]':
        out = []

        for idx in range(num_rows):
            row = [None for _ in range(idx + 1)]
            row[0] = row[-1] = 1

            for jdx in range(1, len(row) - 1):
                row[jdx] = out[idx - 1][jdx - 1] + out[idx - 1][jdx]
            out.append(row)
        return out


def main():
    print(Solution().generate(num_rows=5))


if __name__ == "__main__":
    main()
