"""
Move Zeroes
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        idx = 0
        for index in range(len(nums)):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1

        # x = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[x], nums[i] = nums[i], nums[x]
        #         x += 1
        # print (nums)


def main():
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
    #
    print(Solution().moveZeroes([0, 1, 0, 11, 3]))

    print(Solution().moveZeroes([0, 0, 1]))


if __name__ == "__main__":
    main()
