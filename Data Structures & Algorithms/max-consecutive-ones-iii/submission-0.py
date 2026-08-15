class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        numZeros = 0

        maxLength = 0
        curLength = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1
            
            while numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
                curLength -= 1
            
            curLength += 1
            maxLength = max(maxLength, curLength)
        return maxLength
