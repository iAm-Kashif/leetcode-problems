"""
Palindrome Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(2)
    input1.next.next.next = ListNode(1)
    print(Solution().isPalindrome(input1))


if __name__ == "__main__":
    main()
