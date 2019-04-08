"""
Add Two Numbers
https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/319/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        num1, num2 = str(l1.val), str(l2.val)

        while l1.next:
            num1 += str(l1.next.val)
            l1 = l1.next
        while l2.next:
            num2 += str(l2.next.val)
            l2 = l2.next
        sum = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        tmp = out = ListNode(0)
        for ch in sum:
            out.next = ListNode(ch)
            out = out.next
        return tmp.next




def main():
    input1 = ListNode(2)
    input1.next = ListNode(4)
    input1.next.next = ListNode(3)

    input2 = ListNode(5)
    input2.next = ListNode(6)
    input2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(input1, input2))


if __name__ == "__main__":
    main()
