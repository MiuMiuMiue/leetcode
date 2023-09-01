class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        max_l = 0
        l = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                l += 1
            elif nums[i] != nums[i - 1] + 1 and nums[i] != nums[i - 1]:
                if l > max_l:
                    max_l = l
                l = 1
    
        if l > max_l:
            max_l = l

        return max_l

if __name__ == "__main__":
    s = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]

    print(s.longestConsecutive(nums))
