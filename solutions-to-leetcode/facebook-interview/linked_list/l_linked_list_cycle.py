"""
Linked List Cycle
https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/323/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        else:
            return False


def main():
    input1 = ListNode(2)
    input1.next = ListNode(4)
    input1.next.next = input2 = ListNode(3)
    input1.next.next.next = ListNode(5)
    input1.next.next.next.next = ListNode(6)
    input1.next.next.next.next.next = input2
    print(Solution().hasCycle(input1))


if __name__ == "__main__":
    main()
