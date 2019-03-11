"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1 if root else 0





def main():
    input1 = TreeNode(3)
    input1.left = TreeNode(9)
    input1.right = TreeNode(20)
    input1.right.left = TreeNode(15)
    input1.right.right = TreeNode(7)
    print(Solution().maxDepth(input1.left))

    input2 = TreeNode(1)
    input2.left = TreeNode(2)
    input2.right = TreeNode(3)
    input2.left.left = TreeNode(4)
    input2.right.right = TreeNode(5)
    # print(Solution().maxDepth(input2))


if __name__ == "__main__":
    main()
