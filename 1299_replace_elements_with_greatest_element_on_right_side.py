"""
1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/number-of-islands/

_author:            Kashif Memon
_python_version:    3.8
"""


class Solution:
    def replaceElements(self, arr: 'List[int]') -> 'List[int]':
        out = []

        def process(arr: 'List[int]'):
            if len(arr) == 1: return
            else:
                arr[:] = arr[1:]
                out.append(max(arr))
                process(arr)

        process(arr)
        out.append(-1)

        return out


def main():
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))


if __name__ == "__main__":
    main()
