class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        maxProfit = 0

        for r in range(1,len(prices)):
            while prices[l] > prices[r]:
                l += 1
            maxProfit = max(prices[r] - prices[l], maxProfit)
        return maxProfit


