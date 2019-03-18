"""
Set Matrix Zeroes
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> None:
        zeroes = []
        for item in matrix:
            if 0 in item:
                idx = matrix.index(item)
                jdx = [index for index, value in enumerate(item) if value == 0]
                for val in jdx:
                    zeroes.append((idx, val))
        # print(zeroes)
        for x, y in zeroes:
            for idx in range(len(matrix)):
                matrix[idx][y] = 0
            for jdx in range(len(matrix[0])):
                matrix[x][jdx] = 0
        return matrix


def main():
    input1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(Solution().setZeroes(input1))

    input2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print(Solution().setZeroes(input2))


if __name__ == "__main__":
    main()
