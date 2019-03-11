"""
Delete Node from Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Basically you are given a node which needs to be removed,
        # So, simply take value from the successive node and put in the node to be removed
        # Update pointers so node.next disappears and node becomes node.next (in-a-way)
        node.val = node.next.val
        node.next = node.next.next


def main():
    print(Solution().deleteNode([4, 5, 1, 9]))


if __name__ == "__main__":
    main()
