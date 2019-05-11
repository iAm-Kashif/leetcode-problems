"""
651. 4 Keys Keyboard
https://leetcode.com/problems/4-keys-keyboard/

_author:            Kashif Mem6on
_python_version:    3.7.2
"""


class Solution:
    def maxA(self, N: int) -> int:
        best = [0, 1]
        for k in range(2, N + 1):
            print("k", k)
            best.append(max(best[x] * (k - x - 1) for x in range(k - 1)))
            print("b", best)
            best[-1] = max(best[-1], best[-2] + 1)  # addition
        return best[N]


def main():
    print(Solution().maxA(N=7))


if __name__ == "__main__":
    main()
