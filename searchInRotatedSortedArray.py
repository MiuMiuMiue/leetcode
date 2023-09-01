class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target:
                return pivot

            if nums[pivot] >= nums[left]:
                if target >= nums[left] and target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if target <= nums[right] and target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1