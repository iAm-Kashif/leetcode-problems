"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Codec:

    def encode(self, strs: 'List[str]') -> str:
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s: str) -> 'List[str]':
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j + 1:i])
        return strs


def main():
    print(Codec().encode("hello"))


if __name__ == "__main__":
    main()
