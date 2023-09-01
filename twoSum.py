# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for x in range(len(nums)):
#             for y in range(x + 1, len(nums)):
#                 if (nums[x] + nums[y]) == target:
#                     return [x, y]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for index in range(len(nums)):
            if (target - nums[index]) in visited:
                return [index, visited[target - nums[index]]]
            visited[nums[index]] = index
