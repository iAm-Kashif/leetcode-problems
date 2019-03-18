"""
Group Anagrams
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        out = {}
        for item in strs:
            s_item = "".join(sorted(item))
            if s_item in out:
                out[s_item].append(item)
            else:
                out[s_item] = [item]
        return out.values()

        # Time Limit Exceeded
        # out = []
        # s_strs = []
        # for item in strs:
        #     s_strs.append("".join(sorted(item)))
        #
        # for _ in range(len(set(s_strs))):
        #     item = "".join(sorted(strs[0]))
        #     intermediate = []
        #     val_idx = [index for index, val in enumerate(s_strs) if val == item]
        #     intermediate[:] = [strs[index] for index in val_idx]
        #     strs[:] = [val for idx, val in enumerate(strs) if idx not in val_idx]
        #     s_strs[:] = [val for _, val in enumerate(s_strs) if val != item]
        #     out.append(intermediate)
        # return out


def main():
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
