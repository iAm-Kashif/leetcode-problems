"""
79. Word Search
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        if not board or not word:
            return False
        rows = len(board)
        cols = len(board[0])

        for idx in range(rows):
            for jdx in range(cols):

                if self.checkLetters(board, idx, jdx, word):
                    return True
        return False

    def checkLetters(self, board: 'List[List[str]]', idx: int, jdx: int, word: str) -> bool:
        if len(word) == 0:
            return True
        if idx < 0 or jdx < 0 or idx >=len(board) or jdx >= len(board[0]) or board[idx][jdx] != word[0]:
            return False
        tmp = board[idx][jdx]
        board[idx][jdx] = "#"
        res = self.checkLetters(board, idx + 1, jdx, word[1:]) or \
              self.checkLetters(board, idx - 1, jdx, word[1:]) or \
              self.checkLetters(board, idx, jdx + 1, word[1:]) or \
              self.checkLetters(board, idx, jdx - 1, word[1:])
        board[idx][jdx] = tmp
        return res


def main():
    # board = [
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']
    # ]
    # print(Solution().exist(board, "ABCCED"))
    # print(Solution().exist(board, "SEE"))

    board = [["C", "A", "A"],
             ["A", "A", "A"],
             ["B", "C", "D"]
             ]
    print(Solution().exist(board, "AAB"))


if __name__ == "__main__":
    main()
