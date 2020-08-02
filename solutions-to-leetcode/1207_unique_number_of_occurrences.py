"""
Unique # of occurrences
https://leetcode.com/problems/unique-number-of-occurrences/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def uniqueOccurrences(self, arr: 'List[int]') -> bool:
        dict = {}
        for item in arr:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
        return len(list(dict.values())) == len(list(set(dict.values())))




def main():
    print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    print(Solution().uniqueOccurrences([1, 2]))


if __name__ == "__main__":
    main()
