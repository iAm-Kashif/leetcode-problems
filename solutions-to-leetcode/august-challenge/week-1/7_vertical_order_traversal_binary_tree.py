class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> 'List[List[int]]':
        pass


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.right = TreeNode(3)
    input1.right.left = TreeNode(4)
    input1.right.right = TreeNode(5)
    input1.right.left.left = TreeNode(6)
    input1.right.left.right = TreeNode(7)
    input1.right.left.right.left = TreeNode(8)
    input1.right.left.right.right = TreeNode(9)

    print(Solution().verticalTraversal(input1))


if __name__ == "__main__":
    main()
