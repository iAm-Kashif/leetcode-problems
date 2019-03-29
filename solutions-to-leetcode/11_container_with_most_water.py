"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        start = 0
        end = len(height) - 1
        maxA = 0

        while start < end:
            breadth = min(height[start], height[end])
            length = end - start
            maxA = max(maxA, length * breadth)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxA


def main():
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == "__main__":
    main()
