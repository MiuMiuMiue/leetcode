class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (right + left) // 2
            print(pivot, left, right)
            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1

        return left
if __name__ == "__main__":
    A = Solution()
    nums = [1, 3, 5, 6]
    print(A.searchInsert(nums, 7))
