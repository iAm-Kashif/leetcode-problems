image1 = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0],
]
image2 = [
    [0],
]

image3 = [
    [1],
]


#     [[0,0],[0,0]],
#     [[2,3],[3,5]],
#     [[3,1],[5,1]],
#     [[5,3],[6,4]],
#     [[7,6],[7,6]],


class Solution:
    end = []
    out = []

    def numIslands(self, grid) -> int:

        if not len(grid):
            return 0

        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                val = grid[i][j]

                if val == 0:
                    start = (i, j)
                    self.dfs(grid, i, j)
                    self.end.sort()
                    self.out.append([start, self.end[-1]])
                    self.end.clear()
        return self.out

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0:
            return
        self.end.append((i, j))
        grid[i][j] = "#"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)


print(Solution().numIslands(image1))
