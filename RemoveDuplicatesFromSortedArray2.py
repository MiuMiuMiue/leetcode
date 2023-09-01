class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pt1 = 0
        pt2 = 0

        count = 0
        while pt2 < len(nums):
            if pt1 == pt2 == 0:
                nums[pt1] = nums[pt2]
                pt1 += 1
                pt2 += 1
                count += 1

                continue
            else:
                count = count + 1 if nums[pt2] == nums[pt2 - 1] else 1
            
            if count < 3:
                nums[pt1] = nums[pt2]
                pt1 += 1
                pt2 += 1
            else:
                pt2 += 1

        return pt1

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    
    k = s.removeDuplicates(nums)

    print(k)
    print(nums)
