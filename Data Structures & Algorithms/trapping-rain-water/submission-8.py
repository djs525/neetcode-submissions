class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 1
        r = len(height) - 1

        maxLeft = height[0]
        maxRight = height[len(height)-1]

        waterTrapped = 0
        while l <= r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if maxLeft <= maxRight:
                waterTrapped += maxLeft - height[l]
                l += 1
            
            else:
                waterTrapped += maxRight - height[r]
                r -= 1
        
        return waterTrapped