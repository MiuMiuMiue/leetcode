class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        right = len(nums) - 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                temp = nums[i - 1]

                target = 0
                for j in range(i, len(nums)):
                    if nums[j] > temp and j == len(nums) - 1:
                        target = j
                        break
                    elif nums[j] > temp and nums[j + 1] <= temp:
                        target = j
                        break

                left = i
                nums[i - 1] = nums[target]
                nums[target] = temp

                self.reverse(nums, left, right)
                return

        self.reverse(nums, 0, right)

    def reverse(self, nums, left, right):
        while right > left:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            right -= 1
            left += 1

if __name__ == "__main__":
    A = Solution()
    testList = [1, 2, 3]
    A.nextPermutation(testList)
    print(testList)
