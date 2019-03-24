"""
Jump Over Numbers

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def jump_over_numbers(self, arr: 'List[int]') -> int:
        hops = 0
        pos = 0
        while pos < len(arr):
            if arr[pos] == 0:
                return -1
            pos += arr[pos]
            hops += 1
        return hops


def main():
    print(Solution().jump_over_numbers([3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]))


if __name__ == "__main__":
    main()
