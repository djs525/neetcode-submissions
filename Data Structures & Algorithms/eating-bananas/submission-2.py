class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l+r)//2
            hours = 0
            for i in range(len(piles)):
                if piles[i] % k == 0:
                    hours += piles[i]//k
                else:
                    hours += piles[i]//k + 1            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
