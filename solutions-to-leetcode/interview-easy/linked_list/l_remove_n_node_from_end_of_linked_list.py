"""
Remove Nth Node From End of List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(3)
    input1.next.next.next = ListNode(4)
    input1.next.next.next.next = ListNode(5)
    print(Solution().deleteNode(input1, 2))


if __name__ == "__main__":
    main()
