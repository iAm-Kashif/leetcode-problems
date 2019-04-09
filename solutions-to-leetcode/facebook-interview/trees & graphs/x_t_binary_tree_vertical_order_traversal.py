"""
Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []
        out = []

        while root is not None:
            if not out:
                out.append([root.val])
            else:
                pass


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    input1.left.left = TreeNode(4)
    input1.left.right = TreeNode(5)
    input1.right.left = TreeNode(6)
    input1.right.right = TreeNode(7)
    print(Solution().verticalOrder(input1))


if __name__ == "__main__":
    main()
