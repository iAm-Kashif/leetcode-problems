"""
input: List[]: containing numbers, "a" and "s"
output: sum of all numbers
"a" = Sum of previous 2 numbers
"s" = Skip previous number
"""


def getSum(nums: 'List[int]') -> int:
    L = len(nums)
    sum = 0
    idx = 0

    while idx < L:
        val = nums[idx]

        if val == "a":
            if idx == 0:
                prev_val1 = 0
                prev_val2 = 0
            elif idx == 1:
                prev_val1 = nums[idx - 1]
                prev_val2 = 0
            else:
                prev_val1 = nums[idx - 1]
                prev_val2 = nums[idx - 2]

            nums[idx] = prev_val1 + prev_val2
            sum += nums[idx]

            idx += 1

        elif val == "s":
            if idx == 0:
                prev_val = 0
            else:
                prev_val = nums[idx - 1]

            sum -= prev_val
            if idx == 0:
                del nums[idx]
                idx -= 1
                L -= 1
            else:
                del nums[idx]
                del nums[idx - 1]
                idx -= 2
                L -= 2
            idx += 1

        elif type(val) == int:
            sum += val
            idx += 1

        else:
            print("Not Handled.")

    return sum


input1 = [1, 2, 3, "a", "s", "a"]
input2 = ["s", "s", "a"]

print(getSum(input1))
