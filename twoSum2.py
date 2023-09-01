class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pt1 = 0
        pt2 = len(numbers) - 1

        while True:
            if numbers[pt1] + numbers[pt2] > target:
                pt2 -= 1
            elif numbers[pt1] + numbers[pt2] < target:
                pt1 += 1
            else:
                return [pt1 + 1, pt2 + 1]

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0]
    target = -1

    print(s.twoSum(nums, target))
