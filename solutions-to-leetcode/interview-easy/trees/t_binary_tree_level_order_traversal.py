"""
Binary Tree Level Order Traversal
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    out = []

    def levelOrder(self, root: TreeNode):
        if root is None: return []
        self.out.append([root.val])
        self.traverse(root.left, root.right)

    def traverse(self, left: TreeNode, right: TreeNode):
        if left is not None and right is not None:
            self.out.append([left.val, right.val])
            self.traverse(left.left,)



def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(2)
    input1.left.left = TreeNode(3)
    input1.left.right = TreeNode(4)
    input1.right.left = TreeNode(4)
    input1.right.right = TreeNode(3)
    print(Solution().levelOrder(input1))


if __name__ == "__main__":
    main()
