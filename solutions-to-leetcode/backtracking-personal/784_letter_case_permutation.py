"""
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:

    def letterCasePermutation(self, S: str) -> 'List[str]':
        if not S: return []

        out = [""]
        for ch in S:
            if ch.isdigit():
                out = [item + ch for item in out]
            else:
                out = [item + chr for item in out for chr in [ch.lower(), ch.upper()]]
        return out


def main():
    print(Solution().letterCasePermutation("ab"))


if __name__ == "__main__":
    main()
