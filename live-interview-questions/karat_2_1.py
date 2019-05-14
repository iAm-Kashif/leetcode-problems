# Karat Interview
# Legal Moves and Backtracking.


class Solution1:  # Legal Moves for a player with walls in the grid.
    def legalMoves(self, grid: 'List[List]', player: tuple) -> 'List[tuple]':
        x, y = player[0], player[1]
        out = []

        def positionOnGrid(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        for idx in range(-1, 2, 2):
            if positionOnGrid(x + idx, y):
                if grid[x + idx][y] == 0:
                    out.append((x + idx, y))
            if positionOnGrid(x, y + idx):
                if grid[x][y + idx] == 0:
                    out.append((x, y + idx))

        return out


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
    start1 = (3, 3)
    start2 = (5, 4)
    start3 = (6, 1)
    start4 = (7, 3)
    start5 = (7, 6)
    print(Solution1().legalMoves(image1, start1))
    print(Solution1().legalMoves(image1, start2))
    print(Solution1().legalMoves(image1, start3))
    print(Solution1().legalMoves(image1, start4))
    print(Solution1().legalMoves(image1, start5))


if __name__ == "__main__":
    main()
