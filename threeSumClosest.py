class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        bestSum = 999999999

        for i in range(len(nums) - 1):
            tempSum = 99999999

            st = i + 1
            ed = len(nums) - 1
            while ed != st:
                temp = nums[i] + nums[st] + nums[ed]
                if abs(temp - target) < abs(tempSum - target):
                    tempSum = temp
                elif temp == target:
                    return temp

                if temp < target:
                    st += 1
                else:
                    ed -= 1

            if abs(tempSum - target) < abs(bestSum - target):
                bestSum = tempSum

        return bestSum

if __name__ == "__main__":
    A = Solution()
    print(A.threeSumClosest([-1, 2, 1, -4], 1))