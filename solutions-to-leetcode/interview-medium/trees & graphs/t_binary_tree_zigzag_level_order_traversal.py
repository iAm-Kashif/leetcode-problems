"""
Binary Tree Zigzag Level Order Traversal
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []
        return self.levelOrder(root)

    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        queue = [root]
        final_out = []
        flag = False

        while queue:
            level_out = []
            for _ in range(len(queue)):

                node = queue.pop(0)

                # traverse node children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # add to level_out
                level_out.append(node.val)
            if flag:
                final_out.append(level_out[::-1])
                flag = False
            else:
                final_out.append(level_out)
                flag = True
        return final_out


def main():
    in1 = TreeNode(3)
    in1.left = TreeNode(9)
    in1.right = TreeNode(20)
    in1.right.left = TreeNode(15)
    in1.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(in1))
    # [[3][9, 20] [15,7]]


if __name__ == "__main__":
    main()
