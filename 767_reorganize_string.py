"""
767. Reorganize String
https://leetcode.com/problems/reorganize-string/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def reorganizeString(self, S: str) -> str:

        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            print (c, x)
            if c > (N + 1) / 2: return ""
            A.extend(c * x)
        ans = [None] * N
        idx = int(len(S) / 2)
        ans[::2], ans[1::2] = A[idx:], A[:idx]
        return "".join(ans)

        # from collections import Counter
        # s_map = Counter(S)
        # print (s_map)
        # for item in s_map.values():
        #     if item > (len(S) + 1) / 2:
        #         return ""
        # s_map = sorted(S, key=lambda x: -s_map[x])
        # print (s_map)
        #
        # out = [""] * len(S)
        # idx = int(len(S) / 2)
        # out[::2] = s_map[idx:]
        # out[1::2] = s_map[:idx]
        # return "".join(out)


def main():
    # print(Solution().reorganizeString("aab"))
    #
    # print(Solution().reorganizeString("aaab"))
    #
    # print(Solution().reorganizeString("aabbcczzdef"))

    print(Solution().reorganizeString("abbabbaaab"))



if __name__ == "__main__":
    main()
