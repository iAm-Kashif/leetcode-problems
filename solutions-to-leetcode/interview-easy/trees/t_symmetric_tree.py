"""
Symmetric Tree
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root, root)

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:

        if left is None and right is None:
            return True
        elif left is not None and left is not None:
            if left.val == right.val:
                return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        return False


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(2)
    input1.left.left = TreeNode(3)
    input1.left.right = TreeNode(4)
    input1.right.left = TreeNode(4)
    input1.right.right = TreeNode(3)
    print(Solution().isSymmetric(input1))


if __name__ == "__main__":
    main()
