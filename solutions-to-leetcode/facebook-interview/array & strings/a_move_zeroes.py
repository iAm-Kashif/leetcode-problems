"""
Move Zeroes
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/262/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        idx = 0
        appended = 0
        while idx <= len(nums) - 1 - appended:
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                appended += 1
            else:
                idx += 1
        print(nums)


def main():
    Solution().moveZeroes(nums=[0, 0, 1])
    Solution().moveZeroes(nums=[0, 1, 0, 3, 12])


if __name__ == "__main__":
    main()
