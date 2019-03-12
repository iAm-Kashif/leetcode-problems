"""
Merge 2 Sorted Linked Lists
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        tmp = None
        if l1.val <= l2.val:
            tmp = l1
            tmp.next = self.mergeTwoLists(l1.next, l2)
        else:
            tmp = l2
            tmp.next = self.mergeTwoLists(l1, l2.next)
        return tmp


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
