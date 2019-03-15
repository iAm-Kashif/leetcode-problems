"""
388. Longest Absolute File Path
https://leetcode.com/problems/longest-absolute-file-path/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    pathTable = {-1: 0}
    maxPathLen = 0

    def lengthLongestPath(self, input: str) -> int:
        for line in input.split("\n"):
            dir = line.lstrip("\t")
            depth = len(line) - len(dir)
            # print(line, dir, len(line), len(dir), depth)

            if "." in dir:
                self.maxPathLen = max(self.pathTable[depth - 1] + len(dir), self.maxPathLen)
            else:
                self.pathTable[depth] = self.pathTable[depth - 1] + len(dir) + 1
        return self.maxPathLen

        # Another method is using Stack instead of HashMap for the same reason of adding path lenghts to it.


def main():
    input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(Solution().lengthLongestPath(input1))

    input2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution().lengthLongestPath(input2))


if __name__ == "__main__":
    main()
