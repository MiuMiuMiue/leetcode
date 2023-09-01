class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        index = None
        prev = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] == prev:
                nums[i] = -111
                index = i if index == None else index
            elif nums[i] != prev:
                prev = nums[i]
                length += 1
                if nums[i - 1] == -111:
                    nums[index] = nums[i]
                    nums[i] = -111
                    index += 1
        return length

        # if nums == []:
        #     return 0
        #
        # index = 0
        #
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[index]:
        #         index += 1
        #         nums[index] = nums[i]
        #
        # return index + 1

if __name__ == "__main__":
    testList = [1, 1, 2, 3, 3, 4, 4]

    A = Solution()
    length = A.removeDuplicates(testList)
    print(length, testList)
