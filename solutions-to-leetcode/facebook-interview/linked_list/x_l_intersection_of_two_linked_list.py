"""
Intersection of Two Linked Lists
https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/321/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None

        A, B = headA, headB
        while not A == B:
            if A is None:
                A = headB
            if B is None:
                B = headA
            A = A.next
            B = B.next
        return B.val


def main():
    input1 = ListNode(1)
    input1.next = ListNode(3)
    # input1.next.next = ListNode(3)
    # input1.next.next.next = ListNode(4)
    # input1.next.next.next.next = input2 = ListNode(5)
    # input1.next.next.next.next.next = input2_2 = ListNode(6)

    input2 = ListNode(7)
    input2.next = ListNode(8)
    input2.next.next = ListNode(9)
    input2.next.next.next = input2
    input2.next.next.next.next = input2_2

    print(Solution().getIntersectionNode(input1, input2))


if __name__ == "__main__":
    main()
