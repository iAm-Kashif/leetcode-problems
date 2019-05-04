"""
573. Squirrel Simulation
https://leetcode.com/problems/squirrel-simulation/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def minDistance(self, height: int, width: int, tree: 'List[int]', squirrel: 'List[int]',
                    nuts: 'List[List[int]]') -> int:
        def distanceTwoPoints(pointA, pointB) -> int:
            return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

        pathDistance = sum(2 * distanceTwoPoints(tree, nut) for nut in nuts)
        return pathDistance + min(distanceTwoPoints(squirrel, nut) - distanceTwoPoints(nut, tree) for nut in nuts)


def main():
    print(Solution().minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))


if __name__ == "__main__":
    main()
