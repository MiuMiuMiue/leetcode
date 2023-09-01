class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                temp = self.twoSum(nums[i + 1:], -nums[i])
                if temp != None:
                    for pair in temp:
                        results.append([nums[i], pair[0], pair[1]])
        return results

    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        lookUp = {}
        results = []
        for num in nums:
            if target - num in lookUp and [num, target - num] not in results:
                results.append([num, target - num])
            else:
                lookUp[num] = 1
        print(results)
        return results


if __name__ == "__main__":
    # A = Solution()
    # print(A.threeSum([0, 0, 0, 0]))
    def sumUp(n):
        if n < 10:
            return n
        temp = n % 10
        n //= 10
        return temp + sumUp(n)

    print(sumUp(0))

















