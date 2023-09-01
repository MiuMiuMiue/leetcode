class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if nums == []:
            return 0
        length = len(nums)
        count = 0
        for i in range(len(nums)):
            nums[i - count] = nums[i]
            if nums[i] == val:
                count += 1

        return length - count

if __name__ == "__main__":
    testList = [0, 1, 2, 2, 3, 0, 4, 2]
    A = Solution()
    result = A.removeElement(testList, 2)
    print(result, testList)

