"""
108. Convert Sorted Array to BST
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


def main():
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))


if __name__ == "__main__":
    main()
