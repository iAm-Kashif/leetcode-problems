"""
Swap Node in Pairs
https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        while head is not None and head.next is not None:
            self.swap(head)

    def swap(self, head: ListNode) -> ListNode:
        s


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(3)
    input1.next.next.next = ListNode(4)

    print(Solution().swapPairs())


if __name__ == "__main__":
    main()
