"""
Min Stack
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class MinStack:

    def __init__(self):
        self.out = []
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.out.append(x)

    def pop(self) -> None:
        self.out.pop()

    def top(self) -> int:
        return self.out[len(self.out) - 1]

    def getMin(self) -> int:
        return min(self.out)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
