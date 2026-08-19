class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lcs = 0
        exists = set(nums)
        
        for i in range(len(nums)):
            n = nums[i]
            length = 1
            if n - 1 in exists:
                continue
            
            while n + 1 in exists:
                length += 1
                n = n+1
            lcs = max(lcs,length)
        
        return lcs
        





            
