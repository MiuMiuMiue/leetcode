class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[j]
                nums[j] = 0
                nums[i] = temp
                i += 1

if __name__ == "__main__":
    S = Solution()
    nums = [0,1,0,3,12]
    S.moveZeroes(nums)
    print(nums)
