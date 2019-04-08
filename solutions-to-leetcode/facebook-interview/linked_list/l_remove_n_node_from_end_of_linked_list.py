"""
Remove Nth Node from End of Linked List
https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/320/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = slow = fast = ListNode(0)
        start.next = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return start.next


def main():
    input1 = ListNode(2)
    input1.next = ListNode(4)
    input1.next.next = ListNode(3)
    input1.next.next.next = ListNode(5)
    input1.next.next.next.next = ListNode(6)
    input1.next.next.next.next.next = ListNode(4)
    print(Solution().removeNthFromEnd(input1, 3))


if __name__ == "__main__":
    main()
