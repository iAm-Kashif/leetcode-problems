"""
415. Add Strings
https://leetcode.com/problems/add-strings/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str2int = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        int2str = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

        def convert_to_int(numStr):
            val = []
            for ch in numStr:
                val.insert(0, str2int[ch])
            return "".join(val)

        num1 = convert_to_int(num1)
        num2 = convert_to_int(num1)
        sum = num1 + num2
        val = ""
        for ch in sum:
            val += int2str[ch]
        return val


def main():
    pass


if __name__ == "__main__":
    main()
