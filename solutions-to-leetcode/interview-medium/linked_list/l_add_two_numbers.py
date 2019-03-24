"""
Add 2 Numbers
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = str(l1.val)
        while l1.next:
            num1 += str(l1.next.val)
            l1 = l1.next

        num2 = str(l2.val)
        while l2.next:
            num2 += str(l2.next.val)
            l2 = l2.next

        sum = str(int(num1) + int(num2))[::-1]
        tmp = ListNode(sum[0])
        for i in sum[1:]:
            tmp.next = ListNode(i)
        return tmp


def main():
    num1 = ListNode(2)
    num1.next = ListNode(4)
    num1.next.next = ListNode(3)
    num2 = ListNode(5)
    num2.next = ListNode(6)
    num2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(num1, num2))


if __name__ == "__main__":
    main()
