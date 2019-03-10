"""
Valid Anagram
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if sorted(t) == sorted(s):
            return True
        return False
        # for ichar in s:
        #     if ichar not in t:
        #         return False
        # return True



def main():
    print(Solution().isAnagram("anagram", "nagaram"))

    print(Solution().isAnagram("rat", "car"))

    print(Solution().isAnagram("ab", "a"))


if __name__ == "__main__":
    main()
