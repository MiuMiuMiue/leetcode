class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i - 1]:
                continue
            if i == len(candidates) - 1:
                current = [candidates[i]]
                self.backTracking([], result, current, target)
            else:
                current = [candidates[i]]
                self.backTracking(candidates[i + 1:], result, current, target)
        return result

    def backTracking(self, candidates, combinations, current, target):
        if sum(current) == target:
            combinations.append(current)
        elif sum(current) < target:
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue
                elif sum(current) + candidates[i] > target:
                    break
                if i == len(candidates) - 1:
                    current.append(candidates[i])
                    self.backTracking([], combinations, current[::], target)
                    current.pop()
                else:
                    current.append(candidates[i])
                    self.backTracking(candidates[i + 1:], combinations, current[::], target)
                    current.pop()

if __name__ == "__main__":
    A = Solution()
    testList = [4, 4, 2, 1, 4, 2, 2, 1, 3]
    print(A.combinationSum2(testList, 6))
