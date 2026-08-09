class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1} #remainder : index
        # adding this value ^^ since a good subarray is
        # atleast of length 2. 
        # this prevents it from return a single length subarray
        curSum = 0
        for i,n in enumerate(nums):
            curSum += nums[i]
            r = curSum % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False