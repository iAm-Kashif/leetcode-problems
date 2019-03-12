"""
Reverse Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(3)
    input2 = ListNode(1)
    input2.next = ListNode(3)
    input2.next.next = ListNode(6)
    print(Solution().mergeTwoLists(input1, input2))


if __name__ == "__main__":
    main()
