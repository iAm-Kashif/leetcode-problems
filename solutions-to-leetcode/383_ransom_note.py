"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        try:
            for letter in ransomNote:
                index = magazine.index(letter)
                magazine = magazine[:index] + magazine[index+1:]
        except:
            return False
        return True


def main():
    # print(Solution().canConstruct("a", "b"))
    # print(Solution().canConstruct("aa", "ab"))
    # print(Solution().canConstruct("aa", "aab"))
    print(Solution().canConstruct("gfffbfg", "effjfggbffjdgbjjhhdegh"))


if __name__ == "__main__":
    main()
