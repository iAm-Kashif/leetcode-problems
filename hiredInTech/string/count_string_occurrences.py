"""
Count String Occurrences

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def count(self, T: str, P: str) -> int:
        count = 0
        for idx in range(len(T)-len(P)+1):
            if T[idx: idx+len(P)] == P:
                count += 1
        return count



def main():
    print(Solution().count("babalabalabalatheend", "a"))


if __name__ == "__main__":
    main()
