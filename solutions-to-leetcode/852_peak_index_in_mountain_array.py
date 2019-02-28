"""
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def peakIndexInMountainArray(A: 'List[int]') -> 'int':
    return A.index(max(A))


def main():
    input1 = [0, 1, 0]
    # print(peakIndexInMountainArray(input1))

    input2 = [0, 2, 1, 0]
    # print(peakIndexInMountainArray(input2))

    input3 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
    print(peakIndexInMountainArray(input3))


if __name__ == "__main__":
    main()
