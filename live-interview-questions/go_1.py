"""
Pattern
draw(n):
n = 5
*
**
***
**
*
"""


def draw(n: int) -> None:
    if n < 1: return
    if n == 1:
        print("*")
        return

    for idx in range(1, n // 2 + 1):
        print("*" * idx)

    for idx in range(n // 2 + 1, 0, -1):
        print("*" * idx)


draw(7)
