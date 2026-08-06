class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        lcs = 0
        for num in nums:
            numbers.add(num)
        
        for i in range(len(nums)):
            start = nums[i]
            if start - 1 in numbers:
                continue
            cs = 1
            while start+1 in numbers:
                cs += 1
                start += 1
            lcs = max(cs, lcs)
            
            
        return lcs
            
            