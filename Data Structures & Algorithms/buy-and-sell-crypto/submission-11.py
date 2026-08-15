class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        l = 0
        
        for r in range(1,len(prices)):
            # a loss making situation
            while prices[r] - prices[l] < 0:
                l += 1
            maxProfit = max(maxProfit, (prices[r] - prices[l]))
        return maxProfit
            
            
