"""
942. DI String Match
https://leetcode.com/problems/di-string-match/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def diStringMatch(S: str) -> 'List[int]':
    out = []
    val = 1
    for character in S:
        if character == "I":
            val += 1
        else:
            val -= 1
        out.append(val)
    return out


def main():
    input1 = "IDID"
    print(diStringMatch(input1))

    input2 = "III"
    print(diStringMatch(input2))

    input3 = "D"
    print(diStringMatch(input3))


if __name__ == "__main__":
    main()