"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        key = "%d:%d" % (m, n)
        print (key)
        if key not in self.cache:
            paths = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            self.cache[key] = paths

        return self.cache[key]


def main():
    print(Solution().uniquePaths(3, 2))


if __name__ == "__main__":
    main()
