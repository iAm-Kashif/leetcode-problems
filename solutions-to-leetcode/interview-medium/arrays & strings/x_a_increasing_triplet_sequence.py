"""
Increasing Triplet Subsequence
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:

        for idx in range(len(nums) - 2):
            print(str(nums[idx]) + "<" + str(nums[idx + 1]) + "<" + str(nums[idx + 2]))
            if nums[idx] < nums[idx + 1] < nums[idx + 2]:
                return True
        return False


def main():
    # print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
    # print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
    # print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4]))


if __name__ == "__main__":
    main()
