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
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


def main():
    input1 = ListNode(1)
    input2 = ListNode(2)
    input3 = ListNode(3)
    input4 = ListNode(4)
    input5 = ListNode(5)
    input6 = ListNode(6)
    input7 = ListNode(7)
    input8 = ListNode(8)
    input9 = ListNode(9)
    input10 = ListNode(10)

    input1.next = input2
    input2.next = input3
    input3.next = input4
    input4.next = input5
    input5.next = input6

    input7.next = input8
    input8.next = input9
    input9.next = input5

    print(Solution().getIntersectionNode(input1, input10))


if __name__ == "__main__":
    main()
