"""
21. Merge Two Sorted Linked Lists
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/301/

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
    in1 = ListNode(1)
    in1.next = ListNode(2)
    in1.next.next = ListNode(4)

    in2 = ListNode(1)
    in2.next = ListNode(3)
    in2.next = ListNode(4)
    print(Solution().mergeTwoLists(in1, in2))


if __name__ == "__main__":
    main()
