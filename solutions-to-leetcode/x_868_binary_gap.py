"""
868 Binary Gap
https://leetcode.com/problems/binary-gap/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def binaryGap(self, N: int) -> int:
        list_bin_N = list(bin(N)[2:])
        if list_bin_N.count('1') <= 1:
            return 0
        else:
            print("ELSE")
            idx, jdx = 0, len(list_bin_N) - 1
            while idx < jdx:
                print(idx, jdx)
                if not list_bin_N[idx] == '1':
                    idx += 1

                if not list_bin_N[jdx] == '1':
                    jdx -= 1

                if list_bin_N[idx] == '1' and list_bin_N[jdx] == '1':
                    return jdx - idx


def main():
    print(Solution().binaryGap(N=22))


if __name__ == "__main__":
    main()
