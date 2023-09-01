class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            else:
                if interval[0] <= merged[-1][1]:
                    merged[-1][1] = max(interval[1], merged[-1][1])
                else:
                    merged.append(interval)
        
        return merged
        

if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]

    print(s.insert(intervals, newInterval))
                
                