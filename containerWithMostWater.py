class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        lPt = 0
        rPt = len(height) - 1
        while lPt != rPt:
            width = rPt - lPt
            tempArea = width * min(height[lPt], height[rPt])
            maxArea = tempArea if tempArea > maxArea else maxArea

            if height[lPt] > height[rPt]:
                rPt -= 1
            else:
                lPt += 1
        return maxArea
