"""
Palindrome Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Method_1: Using hashtable (set)
        # if not head: return False
        # nodes = set()
        # while head:
        #     if head in nodes:
        #         return False
        #     nodes.add(head)
        #     head = head.next
        # return True

        # Method_2: Floyd Cycle Algorithm (2-pointer solution)
        # if fast == slow; Cycle exists

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(2)
    input1.next.next.next = ListNode(4)
    input1.next.next.next.next = input1
    print(Solution().hasCycle(input1))


if __name__ == "__main__":
    main()
