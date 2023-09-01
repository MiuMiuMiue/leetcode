class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return nums
        
        start = nums[0]
        seq = 1
        ranges = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq += 1
            else:
                if seq == 1:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                
                start = nums[i]
                
                seq = 1

        if seq == 1:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[i]}")
        
        return ranges

if __name__ == "__main__":
    nums = [0,2,3,4,6,8,9]
    s = Solution()

    print(s.summaryRanges(nums))