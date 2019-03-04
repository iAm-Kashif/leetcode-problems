"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

_author:            Kashif Memon
_python_version:    3.7.2
"""
from collections import Counter


class Solution:
    def checkInclusion_sorting(self, s1: str, s2: str) -> bool:
        sorted_1 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            if sorted_1 in ("".join(sorted(s2[i:i + len(s1)]))):
                return True
        return False

    def checkInclusion_hashmap(self, s1: str, s2: str) -> bool:
        for i in range(0, len(s2) - len(s1) + 1):
            for item in range(len(s1)):
                print (s2[i:i + len(s1)])
                if s1[item] not in s2[i:i + len(s1)]:
                    break
                elif item == (len(s1)-1) and s1[item] in s2[i:i + len(s1)]:
                    return True
                else:
                    continue
        return False


def main():
    s1 = "ab"  # 2
    s21 = "eidbaooo"  # 8
    # print(Solution().checkInclusion_hashmap(s1, s21))

    s22 = "eidboaoo"
    # print(Solution().checkInclusion_hashmap(s1, s22))

    s13 = "adc"  # acd #3
    s23 = "dcda"  # cdd acd # 4
    # print(Solution().checkInclusion_hashmap(s13, s23))

    s14 = "hello"
    s24 = "ooolleoooleh"
    print(Solution().checkInclusion_hashmap(s14, s24))


if __name__ == "__main__":
    main()
