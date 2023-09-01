class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        for num in nums:
            if i != num:
                return i
            i += 1
        return len(nums)

if __name__ == "__main__":
    A = Solution()
    print(A.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
