class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            cur_water = abs(r-l) * min(heights[r],heights[l])
            max_water = max(cur_water, max_water)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_water