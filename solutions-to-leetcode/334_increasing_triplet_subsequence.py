"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:

        first = second = float("inf")
        for val in nums:
            if val <= first:
                first = val
            elif val <= second:
                second = val
            else:
                return True
        return False


def main():
    # print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
    # print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
    # print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4]))


if __name__ == "__main__":
    main()
