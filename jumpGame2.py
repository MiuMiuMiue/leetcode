class Solution:
    def jump(self, nums: list[int]) -> int:
        totalJump = 0

        i = 0
        while i < len(nums) - 1:
            totalJump += 1
            maxStep = nums[i]
            if i + maxStep == len(nums) - 1:
                i += maxStep
            elif i + maxStep > len(nums) - 1:
                i += len(nums) - 1 - i
            else:
                maxRange = i + maxStep + nums[i + maxStep]
                find = False
                index = 0
                for j in range(i + 1, i + maxStep + 1):
                    if j + nums[j] > maxRange:
                        find = True
                        index = j
                        maxRange = j + nums[j]

                if find:
                    i = index
                else:
                    i += maxStep

        return totalJump

if __name__ == "__main__":
    A = Solution()
    print(A.jump([9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]))
