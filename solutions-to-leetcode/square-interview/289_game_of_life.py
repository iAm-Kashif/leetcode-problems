"""
289. Game of Life
https://leetcode.com/problems/game-of-life/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        in-place modification
        LOGIC:
        if cell == 1:
         <2  alive 1->0 | 2
         2-3 alive 1->1 | 1
         >3  alive 1->0 | 2
        if cell == 0:
         3   alive 0->1 | 3
        """
        rows = len(board)
        cols = len(board[0])

        for item in board:
            print(item)

        def get_count(x: int, y: int) -> int:

            count = 0
            for idx in range(x - 1, x + 2):
                for jdx in range(y - 1, y + 2):
                    if not (idx < 0 or jdx < 0 or idx >= rows or jdx >= cols or (idx == x and jdx == y)):
                        val = board[idx][jdx]
                        if val == 1 or val == 2:
                            count += 1
            print("Considering ({}, {} -> {} | {})".format(x, y, board[x][y], count))
            return count

        def process_alive(x: int, y: int) -> int:
            count = get_count(x, y)
            if count < 2 or count > 3:
                board[x][y] = 2
            else:
                board[x][y] = 1

        def process_dead(x: int, y: int) -> int:
            count = get_count(x, y)
            if count == 3:
                board[x][y] = 3

        for idx in range(rows):
            for jdx in range(cols):
                val = board[idx][jdx]

                if val == 1:
                    process_alive(idx, jdx)
                else:
                    process_dead(idx, jdx)

        for idx in range(rows):
            for jdx in range(cols):
                if board[idx][jdx] == 2:
                    board[idx][jdx] = 0
                if board[idx][jdx] == 3:
                    board[idx][jdx] = 1

        for item in board:
            print(item)


def main():
    input1 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print(Solution().gameOfLife(input1))


if __name__ == "__main__":
    main()
