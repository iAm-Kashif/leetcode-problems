"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def checkInclusion_sorting(self, s1: str, s2: str) -> bool:
        sorted_1 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            if sorted_1 in ("".join(sorted(s2[i:i + len(s1)]))):
                return True
        return False

    def checkInclusion_hashmap(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_hashmap = Counter(s1)
        count = len(s1_hashmap)

        print(s1_hashmap, count)

        for index in range(len(s2) - len(s1) + 1):
            subString = s2[index:index + len(s1)]

            for letter in s1_hashmap:
                print("Checking", letter, "in", subString)
                if letter not in subString:
                    break
                for idx in range(s1_hashmap[letter]):




def main():
    s1 = "ab"  # 2
    s21 = "eidbaooo"  # 8
    # print(Solution().checkInclusion_hashmap(s1, s21))

    s22 = "eidboaoo"
    # print(Solution().checkInclusion_hashmap(s1, s22))

    s13 = "addc"  # acd #3
    s23 = "bdcda"  # cdd acd # 4
    print(Solution().checkInclusion_hashmap(s13, s23))

    s14 = "hello"
    s24 = "ooolleoooleh"
    # print(Solution().checkInclusion_hashmap(s14, s24))


if __name__ == "__main__":
    main()
