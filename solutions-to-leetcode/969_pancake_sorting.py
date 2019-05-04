"""
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    out = []

    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        if len(A) == 1: return []
        maxValPos = A.index(max(A))
        A = A[:maxValPos + 1][::-1] + A[maxValPos + 1:]
        A = A[::-1]
        return [maxValPos + 1, len(A)] + self.pancakeSort(A[:-1])

        # My Solution - Wrong apparently
        def flip(idx=None):
            if idx:
                tmp = A[:idx][::-1]
                return tmp + A[idx:]
            return A[::-1]

        if not A: return []
        maxValPos = A.index(max(A)) + 1
        self.out.append(maxValPos)
        A = flip(idx=maxValPos)
        # print("i", A)
        A = flip()
        # print("0", A)
        self.pancakeSort(A[:-1]) + [A[-1]]
        return self.out


def main():
    print(Solution().pancakeSort([1, 2, 3]))
    # print(Solution().pancakeSort([19, 23, 6, 15, 45, 30, 14]))


if __name__ == "__main__":
    main()
