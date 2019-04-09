"""
Find the Celebrity
https://leetcode.com/explore/interview/card/facebook/57/others-3/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        know = {}
        for person_a in range(n):
            know_count = 0
            for person_b in range(n):

                if self.knows(person_a, person_b) == 1:
                    pass


def main():
    print(Solution().findCelebirty([0]))
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()
