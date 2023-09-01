class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        pt1 = 0
        pt2 = 1
        total = nums[pt1]

        while pt2 < len(nums):
            if l == 0:
                while total < target and pt2 < len(nums):
                    total += nums[pt2]
                    pt2 += 1
                if total >= target:
                    l = pt2 - pt1
            else:
                total += nums[pt2]
                pt2 += 1
                total -= nums[pt1]
                pt1 += 1
            
            while total - nums[pt1] >= target:
                total -= nums[pt1]
                pt1 += 1

                if l == 0:
                    l = pt2 - pt1
                elif pt2 - pt1 < l:
                    l = pt2 - pt1

        return l


if __name__ == "__main__":
    s = Solution()
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    
    print(s.minSubArrayLen(target, nums))
