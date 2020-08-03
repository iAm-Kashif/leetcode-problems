"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        visited = ()
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == "1":
                    self.recurse(grid, r, c)
                    count += 1
        return count

    def recurse(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        self.recurse(grid, r + 1, c)
        self.recurse(grid, r - 1, c)
        self.recurse(grid, r, c + 1)
        self.recurse(grid, r, c - 1)


def main():
    input1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "0", "0", "0"]]
    # print(Solution().numIslands(input1))

    input2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
              ["0", "0", "0", "1", "1"]]
    # print(Solution().numIslands(input2))

    image11 = [
        [0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0],
    ]
    print(Solution().numIslands(image11))


if __name__ == "__main__":
    main()
