"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

_author:            Kashif Memon
_python_version:    3.7.2
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: 'ListNode') -> 'bool':
    if not head:
        return False
    tmp = []
    while head.next:
        tmp.append(head)
        if head.next in tmp:
            return True
        tmp.append(head.next)
        head = head.next
    return False


def main():
    input1 = ListNode(3)
    input1.next = ListNode(2)
    input1.next.next = ListNode(0)
    input1.next.next.next = ListNode(-4)
    input1.next.next.next.next = input1.next
    print(hasCycle(input1))

    input2 = ListNode(1)
    input2.next = ListNode(2)
    input2.next = input2
    print(hasCycle(input2))


if __name__ == "__main__":
    main()