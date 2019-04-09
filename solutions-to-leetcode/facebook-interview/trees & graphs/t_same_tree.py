"""
Same Tree
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/306/

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
        if p is None or q is None: return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    print(Solution().isSameTree(input1, input1))

    input21 = TreeNode(1)
    input21.left = TreeNode(3)
    input22 = TreeNode(1)
    input22.right = TreeNode(3)
    # print(Solution().isSameTree(input21, input22))

    input21 = TreeNode(1)
    input21.left = TreeNode(3)
    input22 = TreeNode(1)
    input22.right = TreeNode(3)
    # print(Solution().isSameTree(input21, input22))


if __name__ == "__main__":
    main()
