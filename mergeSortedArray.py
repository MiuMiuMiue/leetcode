class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        pt = (m + n) - 1

        while pt >= 0:
            if i < 0 and j >= 0:
                while j >= 0:
                    nums1[pt] = nums2[j]
                    j -= 1
                    pt -= 1
                break
            elif i >= 0 and j < 0:
                while i >= 0:
                    nums1[pt] = nums1[i]
                    i -= 1
                    pt -= 1
                break
            elif nums1[i] >= nums2[j]:
                nums1[pt] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[pt] = nums2[j]
                j -= 1
            pt -= 1

if __name__ == "__main__":
    S = Solution()
    num1 = [1, 2, 3, 0, 0, 0]
    S.merge(num1, 3, [2, 5, 6], 3)
    print(num1)
