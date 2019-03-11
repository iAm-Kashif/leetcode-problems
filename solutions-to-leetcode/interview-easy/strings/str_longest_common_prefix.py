"""
Longest Common Prefix
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if len(strs) == 0:
            return ""
        word = min(strs, key=len)
        out = ""

        for idx in range(len(word)):
            if all(word[idx] == x[idx] for x in strs):
                out += word[idx]
            else:
                return out
        return out


def main():
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    main()
