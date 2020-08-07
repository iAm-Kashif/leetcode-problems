class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        dict = {}
        for item in nums:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        return [ch for ch, val in dict.items() if dict[ch] > 1]


def main():
    print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == "__main__":
    main()
