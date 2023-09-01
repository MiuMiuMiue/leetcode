# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         values1 = [1]
#         values2 = [1]
#         result = []

#         for i in range(1, len(nums)):
#             values1.append(nums[i - 1] * values1[i - 1])

#         index = 1
#         for i in range(len(nums) - 1, 0, -1):
#             values2.append(nums[i] * values2[index - 1])
#             index += 1

#         values2.reverse()
#         for i in range(len(nums)):
#             result.append(values1[i] * values2[i])

#         return result

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        zeros = 0
        result = [1] * len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total_product *= num

        if zeros > 1:
            return [0] * len(nums)
        elif zeros:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = int(total_product)
                else:
                    result[i] = 0
            return result
        else:
            for i in range(len(nums)):
                    result[i] = int(total_product / nums[i])
            return result


if __name__ == "__main__":
    A = Solution()
    print(A.productExceptSelf([-1,1,0,-3,3]))
