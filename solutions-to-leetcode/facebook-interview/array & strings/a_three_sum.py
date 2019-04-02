"""
Three Sum
https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/283/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return []
        out = []
        nums.sort()

        for idx in range(len(nums) - 2):
            # print(idx, nums[idx])

            if nums[idx] > 0: break
            if idx > 0 and nums[idx] == nums[idx - 1]: continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[idx] + nums[left] + nums[right]
                # print('s', sum)

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    if (nums[idx], nums[left], nums[right]) not in out:
                        out.append((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return out


def main():
    print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
