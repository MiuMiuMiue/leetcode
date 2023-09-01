class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        interval = points[0]

        arrow = 0

        for i in range(1, len(points)):
            if points[i][0] > interval[1]:
                arrow += 1
                interval = points[i]
            else:
                interval = [points[i][0], min(points[i][1], interval[1])]
        
        return arrow + 1

if __name__ == "__main__":
    s = Solution()
    points = [[1,2],[2,3],[3,4],[4,5]]
    points.sort(key=lambda x:x[1])
    print(points)

    print(s.findMinArrowShots(points))
