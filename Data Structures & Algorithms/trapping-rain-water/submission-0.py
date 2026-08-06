class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        count = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                count += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                count += maxRight - height[r]

            
        return count
            