"""
Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# Recursive approach
class Solution:
    def verticalOrder(self, root: TreeNode) -> 'List[List[int]]':
        distance = 0
        import collections
        nodeMap = collections.defaultdict(list)

        def traverse(node: TreeNode, hd: int):
            if not node: return

            nodeMap[hd].append(node.val)

            if node.left:
                traverse(node.left, hd - 1)
            if node.right:
                traverse(node.right, hd + 1)

        traverse(root, distance)
        return [val for _, val in sorted(nodeMap.items())]


# Queue based approach
class Solution1:
    def verticalOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []

        import collections
        out = collections.defaultdict(list)
        queue = [(root, 0)]

        for node, distance in queue:
            out[distance].append(node.val)

            if node.left:
                queue.append((node.left, distance - 1))
            if node.right:
                queue.append((node.right, distance + 1))
        return [sorted(val) for _, val in sorted(out.items())]


def main():
    input1 = TreeNode(3)
    input1.left = TreeNode(9)
    input1.right = TreeNode(8)
    input1.left.left = TreeNode(4)
    input1.left.right = TreeNode(0)
    input1.right.left = TreeNode(1)
    input1.right.right = TreeNode(7)
    print(Solution().verticalOrder(input1))


if __name__ == "__main__":
    main()
