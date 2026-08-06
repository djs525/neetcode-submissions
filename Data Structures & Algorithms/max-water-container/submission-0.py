class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = float('-inf')
        while l<r:
            if heights[l] < heights[r]:
                area = (r-l)*heights[l]
                l+=1
            elif heights[l] > heights[r]:
                area = (r-l)*heights[r]
                r-=1
            else:
                area = (r-l)*heights[l]
                l+=1
                r-=1
                
            maxArea = max(maxArea, area)
        return maxArea