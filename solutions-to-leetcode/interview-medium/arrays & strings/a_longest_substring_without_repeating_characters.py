"""
Longest Substring Without Repeating Characters
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        tmp = []
        for ch in s:
            if ch in tmp:
                tmp = tmp[tmp.index(ch) + 1:]
                tmp.append(ch)
            else:
                tmp.append(ch)
            maxLen = max(maxLen, len(tmp))
        return maxLen


def main():
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring(" "))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))


if __name__ == "__main__":
    main()
