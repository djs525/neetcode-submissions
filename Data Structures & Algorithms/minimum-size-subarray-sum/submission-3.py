class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = float('inf')
        curSum = 0
        curLength = 0

        for r in range(len(nums)):
            curSum += nums[r]
            curLength += 1
            while curSum >= target:
                minLength = min(minLength, curLength)
                curSum -= nums[l]
                curLength -= 1
                l += 1
            
        return minLength if minLength != float('inf') else 0