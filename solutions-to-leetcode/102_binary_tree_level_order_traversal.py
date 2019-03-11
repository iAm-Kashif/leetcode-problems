"""
102. Binary Tree Level Order Traversal
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
    queue = []
    final_out = []
    level_out = []

    def __init__(self):
        self.queue.clear()
        self.final_out.clear()
        self.level_out.clear()

    def levelOrder(self, root: TreeNode):
        if root is None: return []

        self.queue.append(root)
        while self.queue:
            self.levelTraverse()
            self.final_out.append(self.level_out)
        # print(">>F:", self.final_out)
        return self.final_out

    def levelTraverse(self):
        self.level_out = []
        for idx in range(len(self.queue)):
            node = self.queue.pop(0)
            self.level_out.append(node.val)
            if node.left is not None:
                self.queue.append(node.left)
            if node.right is not None:
                self.queue.append(node.right)
        # print(">>L:", self.level_out)


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    input1.left.left = TreeNode(4)
    input1.left.right = TreeNode(5)
    input1.right.left = TreeNode(6)
    input1.right.right = TreeNode(7)
    print(Solution().levelOrder(input1))

    input2 = TreeNode(3)
    input2.left = TreeNode(9)
    input2.right = TreeNode(20)
    input2.right.left = TreeNode(15)
    input2.right.right = TreeNode(7)
    print(Solution().levelOrder(input2))


if __name__ == "__main__":
    main()
