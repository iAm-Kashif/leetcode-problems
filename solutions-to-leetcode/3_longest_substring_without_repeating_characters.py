"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        curr = ""

        for idx in range(len(s)):
            ch = s[idx]

            if ch not in curr:
                curr += ch
            else:
                maxlen = max(len(curr), maxlen)
                pos = curr.index(ch)
                curr = curr[pos + 1:] + ch
        maxlen = max(len(curr), maxlen)
        return maxlen


def main():
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))

    print(Solution().lengthOfLongestSubstring(s="bbbbb"))

    print(Solution().lengthOfLongestSubstring(s="pwwkew"))


if __name__ == "__main__":
    main()
