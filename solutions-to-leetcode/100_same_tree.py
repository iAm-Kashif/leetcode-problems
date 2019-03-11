"""
100. Same Tree
https://leetcode.com/problems/same-tree/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is not None and q is None: return False
        if p is None and q is not None:
            return False
        elif p is not None and q is not None:
            return self.isSame(p, q)

    def isSame(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is not None and q is None: return False
        if p is None and q is not None: return False
        if p.left is None and q.left is not None: return False
        if p.left is not None and q.left is None: return False
        if p.left is None and q.left is not None: return False
        if p.left is not None and q.left is None: return False
        if not p.val == q.val: return False
        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    print(Solution().isSameTree(input1, input1))

    input21 = TreeNode(1)
    input21.left = TreeNode(3)
    input22 = TreeNode(1)
    input22.right = TreeNode(3)
    print(Solution().isSameTree(input21, input22))

    input21 = TreeNode(1)
    input21.left = TreeNode(3)
    input22 = TreeNode(1)
    input22.right = TreeNode(3)
    print(Solution().isSameTree(input21, input22))


if __name__ == "__main__":
    main()
