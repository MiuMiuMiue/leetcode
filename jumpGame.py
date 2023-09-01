class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) > 1 and nums[0] == 0:
            return False
        elif nums[0] == 0:
            return True

        for i in range(len(nums)):

            if nums[i] == 0:
                j = i - 1
                step = 2
                while j >= 0:
                    if nums[j] >= step or (nums[j] == step - 1 and i == len(nums) - 1):
                        break
                    step += 1
                    j -= 1

                if j < 0:
                    return False
        
        return True

if __name__ == "__main__":
    nums = [3,0,0,0]
    s = Solution()

    print(s.canJump(nums))
