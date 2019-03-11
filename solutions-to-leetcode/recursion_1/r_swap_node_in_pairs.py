"""
Swap Node in Pairs
https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return None
        if head.next is None: return head

        cur_node = head.next
        next_node = self.swapPairs(cur_node.next)
        head.next = next_node
        cur_node.next = head
        return cur_node


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(3)
    input1.next.next.next = ListNode(4)

    print(Solution().swapPairs(input1))


if __name__ == "__main__":
    main()
