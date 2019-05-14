# Karat Interview
# Check if from every open position in the grid, can the end position be reached.


class Solution1:  # Legal Moves for a player with walls in the grid.
    # This solution starts with the end location
    # propogates in all 4 directions to find all positions that it can reach
    # Once done, if 0 in grid -> that means it cannot be reached -> return False

    def canReach(self, grid: 'List[List]', start: tuple) -> bool:
        x, y = start[0], start[1]

        def positionOnGrid(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        def updateCell(x: int, y: int) -> bool:
            if grid[x][y] == 0:
                grid[x][y] = "*"

        def backtrack(x: int, y: int):
            while positionOnGrid(x, y) and grid[x][y] == 0:
                updateCell(x, y)
                backtrack(x + 1, y)
                backtrack(x - 1, y)
                backtrack(x, y + 1)
                backtrack(x, y - 1)

        backtrack(x, y)

        for item in grid:
            if 0 in item:
                return False
        else:
            return True


def main():
    image1 = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 0, -1, -1, -1],
        [-1, -1, -1, -1, 0, -1, -1],
        [-1, -1, -1, 0, 0, -1, -1],
        [-1, 0, 0, 0, 0, -1, -1],
        [-1, 0, -1, 0, 0, 0, 0]
    ]
    end = (7, 3)
    print(Solution2().canReach(image1, end))


if __name__ == "__main__":
    main()
