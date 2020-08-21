class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = jdx = 0
        nums1 = nums1[:-n]
        print(nums1)
        while idx <= m+n and jdx <= n:
            print("Considering", nums1[idx], "XXX", nums2[jdx], "idx", idx, "jdx", jdx)
            print(nums1)
            if nums1[idx] <= nums2[jdx]:
                idx += 1
            else:
                nums1.insert(idx, nums2[jdx])
                idx += 1
                jdx += 1

        return nums1


def main():
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


if __name__ == "__main__":
    main()
