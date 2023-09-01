class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num3 = sorted(nums1 + nums2)
        length = len(num3)
        if (length) % 2 == 1:
            return num3[length // 2]
        else:
            return (num3[length // 2] + num3[length // 2 - 1]) / 2