"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(head: 'ListNode') -> 'ListNode':
    tmp = [head]
    while head.next:
        tmp.append(head.next)
        head = head.next
    return tmp.pop(int((len(tmp))/2))


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(3)
    input1.next.next.next = ListNode(4)
    input1.next.next.next.next = ListNode(5)
    # print(middleNode(input1))

    input2 = ListNode(1)
    input2.next = ListNode(2)
    input2.next.next = ListNode(3)
    input2.next.next.next = ListNode(4)
    input2.next.next.next.next = ListNode(5)
    input2.next.next.next.next.next = ListNode(6)
    # print(middleNode(input2))


if __name__ == "__main__":
    main()