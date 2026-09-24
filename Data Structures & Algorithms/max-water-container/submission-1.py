class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pt1 = 0
        pt2 = len(heights)-1
        maxArea = 0

        while pt1 < pt2:
            newArea = min(heights[pt1], heights[pt2])*(pt2-pt1)
            maxArea = max(maxArea, newArea)
            if heights[pt1] > heights[pt2]:
                pt2 -= 1
            else:
                pt1 += 1
        
        return maxArea

        