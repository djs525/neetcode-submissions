class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        if not nums:
            return 0
        
        numSet = set(nums)
        
        longest = 1

        i = 0
        while i < len(nums):
            n = nums[i]
            if (n-1) not in numSet:
                curLength = 0
                while n in numSet:
                    curLength += 1
                    n += 1
                
            
                longest = max(longest, curLength)
            i += 1
        
        return longest
        

