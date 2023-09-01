class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        for i in range(len(candidates)):
            current = [candidates[i]]
            self.backTracking(candidates[i:], result, current, target)
        return result

    def backTracking(self, candidates, combinations, current, target):
        if sum(current) == target:
            combinations.append(current)
        elif sum(current) < target:
            for i in range(len(candidates)):
                current.append(candidates[i])
                self.backTracking(candidates[i:], combinations, current[::], target)
                current.pop()

if __name__ == "__main__":
    A = Solution()
    testList = [2, 3, 6, 7]
    print(A.combinationSum(testList, 7))
