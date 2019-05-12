"""
36. Valid Sodoku
https://leetcode.com/problems/valid-sudoku/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> None:
        self.board = board
        return self.solve()

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        # print("isSafe():")
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        # print("checkRow():")
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        # print("checkCol():")
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        # print("checkSq():")
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True

    def solve(self):
        for r in range(9):
            for c in range(9):
                val = self.board[r][c]
                # print(">>Considering {},{}: {}".format(r, c, val))
                self.board[r][c] = "."
                if not val == ".":
                    if not self.isSafe(r, c, val):
                        return False
                self.board[r][c] = val
        return True


def main():
    input1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(input1))


if __name__ == "__main__":
    main()
