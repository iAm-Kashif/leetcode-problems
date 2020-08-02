"""
1. Two Sum
https://leetcode.com/problems/two-sum/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]], i]
    else:
        dict[target - nums[i]] = i
    """
    for index in range(len(nums)):
        if (target - nums[index]) in nums:
            if index == nums.index(target-nums[index]):
                continue
            else:
                return [index, nums.index(target-nums[index])]
    """


def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9
    # print(twoSum(nums1, target1))

    nums2 = [3, 2, 3]
    target2 = 6
    print(twoSum(nums2, target2))


if __name__ == "__main__":
    main()
