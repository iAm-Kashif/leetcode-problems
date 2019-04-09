"""
Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/305/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if not inorder: return
        rootVal = preorder.pop(0)
        rootNode = TreeNode(rootVal)
        index = inorder.index(rootVal)
        left, right = inorder[:index], inorder[index + 1:]
        rootNode.left = self.buildTree(preorder, left)
        rootNode.right = self.buildTree(preorder, right)
        return rootNode


def main():
    inorder = [10, 30, 40, 50, 60, 70, 90]
    preorder = [50, 30, 10, 40, 70, 60, 90]
    print(Solution().buildTree(inorder, preorder))


if __name__ == "__main__":
    main()
