"""
573. Squirrel Simulation
https://leetcode.com/problems/squirrel-simulation/

_author:            Kashif Memon
_python_version:    3.7.2
"""

"""
Explanation:
Let D be the taxicab distance, D(P, Q) = abs(Px - Qx) + abs(Py - Qy).

Suppose the squirrel is already at the tree. The distance of his path will be:
S = D(tree, nut_1) + D(nut_1, tree) + D(tree, nut_2) + D(nut_2, tree) + D(tree, nut_3) + ...
and so
S = sum_{i=1..N} 2 * D(tree, nut_i).

At the beginning, the squirrel goes to some nut_k, then to the tree, then does the usual path described above except doesn't visit nut_k. Thus, his path has distance:
D(squirrel, nut_k) + D(nut_k, tree) + S - (2 * D(tree, nut_k))
which equals
S + D(squirrel, nut_k) - D(nut_k, tree).
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
