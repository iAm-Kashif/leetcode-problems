"""
599. Minimum Index Sum of Two Lists
https://leetcode.com/problems/minimum-index-sum-of-two-lists/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        out = []
        min_idxSum = float("inf")

        for item in list(set(list2).intersection(set(list1))):
            print(item, list1.index(item), list2.index(item), min_idxSum)
            idx_sum = list1.index(item) + list2.index(item)
            if idx_sum < min_idxSum:
                min_idxSum = idx_sum
                out = [item]
            elif idx_sum == min_idxSum:
                out.append(item)
        return out






def main():
    l11 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    l12 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    # print(Solution().findRestaurant(l11, l12))

    l21 = ["Shogun","Tapioca Express","Burger King","KFC"]
    l22 = ["KFC", "Shogun", "Burger King"]
    print(Solution().findRestaurant(l21, l22))

if __name__ == "__main__":
    main()
