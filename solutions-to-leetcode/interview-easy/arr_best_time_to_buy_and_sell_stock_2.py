"""
Best Time to Buy and Sell Stock II
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        profit = 0
        for i in range(1, len(prices)):
            val = prices[i] - prices[i - 1]
            if val > 0:
                profit += val
        return profit


def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

    print(Solution().maxProfit([1, 2, 3, 4, 5]))

    print(Solution().maxProfit([7, 6, 4, 3, 1]))


if __name__ == "__main__":
    main()
