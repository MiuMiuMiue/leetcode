class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = []
        for i in range(0, len(nums)):
            if i < k:
                queue.append(nums[i])
                nums[i] = nums[len(nums) - k + i]
            else:
                queue.append(nums[i])
                nums[i] = queue.pop(0)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    s = Solution()
    s.rotate(nums, k)
    print(nums)
