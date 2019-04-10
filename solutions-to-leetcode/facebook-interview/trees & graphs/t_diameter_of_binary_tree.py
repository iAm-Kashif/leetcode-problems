"""
Diameter of Binary Tree
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/291/

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
        def traverse(root: TreeNode) -> int:
            if not root: return 0
            left = traverse(root.left)
            right = traverse(root.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        self.diameter = 0
        traverse(root)
        return self.diameter


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    input1.left.left = TreeNode(4)
    input1.left.right = TreeNode(7)
    input1.left.right.right = TreeNode(8)
    input1.left.right.right.right = TreeNode(9)
    input1.left.right.right.right.right = TreeNode(10)
    input1.left.left.left = TreeNode(5)
    input1.left.left.left.left = TreeNode(6)
    print(Solution().diameterOfBinaryTree(input1))


if __name__ == "__main__":
    main()
