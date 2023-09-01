class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > results[-1][1]:
                results.append(intervals[i])
            else:
                results[-1][1] = max(results[-1][1], intervals[i][1])
        
        return results

if __name__ == "__main__":
    s = Solution()
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

    print(s.merge(intervals))
