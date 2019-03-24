"""
Intersection of Two Linked Lists
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB

        while not curA == curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA


def main():
    in1 = ListNode(4)
    in1.next = ListNode(1)
    intersect1 = ListNode(8)
    intersect1.next = ListNode(4)
    intersect1.next.next = ListNode(5)
    in1.next.next = intersect1
    in2 = ListNode(5)
    in2.next = ListNode(0)
    in2.next.next = ListNode(1)
    in2.next.next.next = ListNode(10)
    print(Solution().getIntersectionNode(in1, in2))


if __name__ == "__main__":
    main()
