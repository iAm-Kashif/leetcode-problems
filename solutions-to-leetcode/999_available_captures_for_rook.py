"""
999. Available Captures for Rook
https://leetcode.com/problems/available-captures-for-rook/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    out = 0

    def numRookCaptures(self, board: 'List[List[str]]') -> int:

        def find_position_of_rook():
            for idx in range(8):  # rows
                for jdx in range(8):  # cols
                    if board[idx][jdx] == "R":
                        return idx, jdx

        rook = find_position_of_rook()

        def capture_pawns(x: int, y: int, ):
            print("Considering>> ({}, {})".format(x, y))
            if x < 0 or y < 0 or x > 7 or y > 7 or board[x][y] == "B": return
            if board[x][y] == "p":
                self.out += 1
                return
            elif board[x][y] == ".":
                if x == rook[0]:
                    if y > rook[1]:
                        capture_pawns(x, y + 1)
                    else:
                        capture_pawns(x, y - 1)
                else:
                    if x > rook[0]:
                        capture_pawns(x + 1, y)
                    else:
                        capture_pawns(x - 1, y)

            elif board[x][y] == "R":  # first run only.
                capture_pawns(x + 1, y)
                capture_pawns(x - 1, y)
                capture_pawns(x, y + 1)
                capture_pawns(x, y - 1)

        capture_pawns(rook[0], rook[1])
        return self.out


def main():
    input1 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    print(Solution().numRookCaptures(input1))

    input2 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
              [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
              [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    print(Solution().numRookCaptures(input2))

    input3 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    print(Solution().numRookCaptures(input3))


if __name__ == "__main__":
    main()
