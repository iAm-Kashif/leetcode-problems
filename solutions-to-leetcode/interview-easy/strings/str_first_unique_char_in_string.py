"""
First Unique Character in a String
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for item in s:
            if s.count(item) == 1:
                return s.index(item)
        return -1

        # Using collections.Counter()
        # from collections import Counter
        # for char, val in Counter(s).items():
        #     if val == 1:
        #         return s.index(char)
        # return -1


def main():
    print(Solution().firstUniqChar("leetcode"))

    print(Solution().firstUniqChar("loveleetcode"))


if __name__ == "__main__":
    main()
