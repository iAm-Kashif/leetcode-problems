"""
Number of Islands
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid: return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for idx in range(rows):
            for jdx in range(cols):
                val = grid[idx][jdx]
                # print("Considering ({}, {}): {}".format(idx, jdx, val))

                if val == "1":
                    self.dfs(grid, idx, jdx)
                    islands += 1
        return islands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


def main():
    input1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(input1))

    input2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
              ["0", "0", "0", "1", "1"]]
    # print(Solution().numIslands(input2))


if __name__ == "__main__":
    main()
