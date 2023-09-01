class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = (right + left) // 2
            if nums[pivot] == target:
                start = pivot
                while nums[start] == target and start > 0:
                    start -= 1
                start = start if start == 0 and nums[start] == target else start + 1
                end = pivot
                while nums[end] == target and end < len(nums) - 1:
                    end += 1
                end = end if end == len(nums) - 1 and nums[end] == target else end - 1
                return [start, end]
            if nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return [-1, -1]

if __name__ == "__main__":
    A = Solution()
    print(A.searchRange([5, 7, 7, 8, 8, 10], 8))