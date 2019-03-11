"""
Validate Binary Search Tree
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

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
        if root is None:
            return True

        return self.isBST(root, float("-inf"), float("inf"))

    def isBST(self, root: TreeNode, low, high) -> bool:
        if root is None:
            return True
        if not low < root.val < high: return False
        return self.isBST(root.left, low, root.val) and self.isBST(root.right, root.val, high)


def main():
    input1 = TreeNode(3)
    input1.left = TreeNode(9)
    input1.right = TreeNode(20)
    input1.right.left = TreeNode(15)
    input1.right.right = TreeNode(7)
    print(Solution().isValidBST(input1))

    input2 = TreeNode(5)
    input2.left = TreeNode(1)
    input2.right = TreeNode(4)
    input2.left.left = TreeNode(3)
    input2.right.right = TreeNode(4)
    # print(Solution().isValidBST(input2))

    input3 = TreeNode(2)
    input3.left = TreeNode(1)
    input3.right = TreeNode(3)
    print(Solution().isValidBST(input3))


if __name__ == "__main__":
    main()
