"""
Reverse Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return []
        before, current = None, head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    out = Solution().reverseList(input1)
    print(out.val, out.next.val)


if __name__ == "__main__":
    main()
