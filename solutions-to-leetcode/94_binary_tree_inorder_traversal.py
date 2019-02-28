"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    out = []

    def inorderTraversal(self, root: TreeNode) -> 'List[int]':
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)) if root else []
        # if root:
        #     if root.val == "null":
        #         return
        #     self.inorderTraversal(root.left)
        #     self.out.append(root.val)
        #     self.inorderTraversal(root.right)
        # return self.out


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode("null")
    input1.right = TreeNode(2)
    input1.right.left = TreeNode(3)
    print(Solution().inorderTraversal(input1))


if __name__ == "__main__":
    main()
