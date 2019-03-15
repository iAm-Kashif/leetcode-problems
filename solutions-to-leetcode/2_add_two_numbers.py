"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

_author:            Kashif Memon
_python_version:    3.7.2
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    num1 = str(l1.val)
    num2 = str(l2.val)
    while l1.next:
        num1 += str(l1.next.val)
        l1 = l1.next
    while l2.next:
        num2 += str(l2.next.val)
        l2 = l2.next
    sum = int(num1[::-1]) + int(num2[::-1])
    sum = str(sum)[::-1]
    tmp = ListNode(0)
    tmp.next = out = ListNode(sum[0])
    for i in sum[1:]:
        out.next = ListNode(i)
        out = out.next
    return tmp.next


def main():
    input11 = ListNode(2)
    input11.next = ListNode(4)
    input11.next.next = ListNode(3)
    input12 = ListNode(5)
    input12.next = ListNode(6)
    input12.next.next = ListNode(4)
    print(addTwoNumbers(input11, input12))


if __name__ == "__main__":
    main()
