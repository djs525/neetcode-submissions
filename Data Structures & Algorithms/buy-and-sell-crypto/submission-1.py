class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        l=0
        for r in range(1,len(prices)):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
            else:
                l = r
                profit = 0
            
            maxProfit = max(profit, maxProfit)
        return maxProfit

            
            

                

            
            

            