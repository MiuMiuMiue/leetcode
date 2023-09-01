import collections


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        testDict = collections.defaultdict(int)
        result = []
        for i in range(len(nums)):
            if i < len(nums) - 1:
                tempResult = self.threeSum(nums[i + 1:], target - nums[i])
                if tempResult != []:
                    for pair in tempResult:
                        pair.append(nums[i])
                        if testDict[tuple(sorted(pair))] == 0:
                            result.append(pair)
                            testDict[tuple(sorted(pair))] += 1
        return result

    def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        for i in range(len(nums)):
            if i < len(nums) - 1:
                tempResult = self.twoSum(nums[i + 1:], target - nums[i])
                if tempResult != []:
                    for pair in tempResult:
                        pair.append(nums[i])
                        result.append(pair)
        return result

    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        testDict = {}
        result = []
        for num in nums:
            if target - num in testDict:
                result.append([num, target - num])
            else:
                testDict[num] = 0
        return result

if __name__ == "__main__":
    A = Solution()
    print(A.fourSum([2, 2, 2, 2, 2], 8))
