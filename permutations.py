class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def findPermutation(exist, current):
            if len(current) == len(nums):
                result.append(current)
                return

            for j in range(len(nums)):
                if j not in exist:
                    exist.append(j)
                    current.append(nums[j])
                    findPermutation(exist, current[::])
                    current.pop()
                    exist.pop()

        for i in range(len(nums)):
            current = [nums[i]]
            exist = [i]
            findPermutation(exist, current[::])

        return result

if __name__ == "__main__":
    A = Solution()
    print(A.permute([1, 2, 3]))