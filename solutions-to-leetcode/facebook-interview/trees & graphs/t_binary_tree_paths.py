"""
Binary Tree Paths
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/280/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> 'List[str]':
        # Recursive approach

        def calculate_paths(path: str, node: TreeNode):
            path += "->" + str(node.val)
            if not node.right and not node.left:
                out.append(path[2:])
                return

            if node.right:
                calculate_paths(path, node.right)

            if node.left:
                calculate_paths(path, node.left)

        if not root: return []
        out = []
        calculate_paths("", root)
        return out

        # Iterative approach using Stack
        # if not root: return []
        #
        # stack = [(root, str(root.val))]
        # out = []
        #
        # while stack:
        #     node = stack.pop()
        #
        #     if not node[0].right and not node[0].left:
        #         out.append(node[1])
        #
        #     if node[0].right:
        #         stack.append((node[0].right, node[1] + "->" + str(node[0].right.val)))
        #     if node[0].left:
        #         stack.append((node[0].left, node[1] + "->" + str(node[0].left.val)))
        # return out


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.left.left = TreeNode(3)
    input1.left.right = TreeNode(4)
    input1.right = TreeNode(5)
    input1.right.right = TreeNode(6)
    print(Solution().binaryTreePaths(input1))


if __name__ == "__main__":
    main()
