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
    def isPalindrome_1(self, head: ListNode) -> bool:
        # Method 1 - Stack
        # Iterate over list, add to Stack
        # Iterate again and check pop() stack contents
        # True if all match ,else False
        if head is None: return True
        curr = head
        stack = []
        while curr is not None:
            print(">> Adding to Stack", curr.val)
            stack.append(curr)
            curr = curr.next

        while head is not None and not len(stack) == 0:
            if not head.val == (stack.pop()).val:
                return False
            head = head.next
        return True

        # Method 2 - Reverse List
        # Figure middle of list
        # Reverse from middle of list
        # verify if new reverse and middle is same?

    def isPalindrome_2(self, head: ListNode) -> bool:
        # Method 3 - Recursive
        
        pass


def main():
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(2)
    input1.next.next.next = ListNode(0)
    print(Solution().isPalindrome(input1))


if __name__ == "__main__":
    main()
