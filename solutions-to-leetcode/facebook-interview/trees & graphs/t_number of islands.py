"""
Number of Islands
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/274/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def numIslands(self, grid) -> int:
        if not grid: return 0

        def traverse(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or not grid[i][j] == "1":
                return
            grid[i][j] = "#"
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for idx in range(rows):
            for jdx in range(cols):
                val = grid[idx][jdx]

                if val == "1":
                    traverse(idx, jdx)
                    count += 1
        return count


def main():
    input1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(input1))

    input2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
              ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(input2))


if __name__ == "__main__":
    main()
