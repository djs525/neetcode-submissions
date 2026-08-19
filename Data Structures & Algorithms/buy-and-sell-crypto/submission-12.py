class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            
            curProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, curProfit)
        
        return maxProfit