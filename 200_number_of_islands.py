"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def numIslands(self, grid) -> int:

        if not len(grid):
            return 0

        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                val = grid[i][j]
                print(">> Considering({},{}); Val: {}".format(i, j, val))

                if val == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

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
    print(Solution().numIslands(input2))



if __name__ == "__main__":
    main()
