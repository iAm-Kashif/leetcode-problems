"""
Binary Tree Paths
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/280/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, root: TreeNode, low, high) -> bool:
        if not root: return True
        if not low < root.val < high: return False
        return self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)


def main():
    input1 = TreeNode(2)
    input1.left = TreeNode(1)
    input1.right = TreeNode(3)
    print(Solution().isValidBST(input1))


if __name__ == "__main__":
    main()
