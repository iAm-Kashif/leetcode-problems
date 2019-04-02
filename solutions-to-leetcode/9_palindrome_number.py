"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        else: return x == int(str(x)[::-1])


def main():
    nums11 = [1, 3]
    nums12 = [2]
    # print("The median is", findMedianSortedArrays(nums11, nums12))

    nums21 = [1, 2]
    nums22 = [3, 4]
    print("The median is", findMedianSortedArrays(nums21, nums22))


if __name__ == "__main__":
    main()
