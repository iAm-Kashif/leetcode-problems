"""
Rotate Array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        for i in range(k):
            nums[:] = [nums[-1]] + nums[:-1]
        return nums

        # also works by segmented list assignment.
        # nums[0:k], nums[k:] = nums[(len(nums) - k):], nums[0:(len(nums) - k)]


def main():
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))

    print(Solution().rotate([-1, -100, 3, 99], 2))

    print(Solution().rotate([1, 2], 3))


if __name__ == "__main__":
    main()
