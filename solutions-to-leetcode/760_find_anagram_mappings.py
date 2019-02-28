"""
760. Find Anagram Mappings
Locked.

_author:            Kashif Memon
_python_version:    3.7.2
"""


def anagramMappings(A: 'List[int]', B: 'List[int]') -> 'List[int]':
    out = []
    for item in A:
        out.append(B.index(item))
    return out


def main():
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    print(anagramMappings(A, B))


if __name__ == "__main__":
    main()
