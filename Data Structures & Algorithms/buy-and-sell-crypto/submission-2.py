class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
            else:
                l=r
                profit = 0
            max_profit = max(profit, max_profit)
        return max_profit
            
            

            