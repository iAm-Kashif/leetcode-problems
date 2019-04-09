"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        pass


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    input1.left.left = TreeNode(4)
    input1.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(input1))


if __name__ == "__main__":
    main()
