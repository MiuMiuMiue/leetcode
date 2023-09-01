class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        result = 1
        for i in range(len(nums)):
            if nums[i] == result:
                result += 1

        return result