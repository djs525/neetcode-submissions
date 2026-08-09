class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1} #sum : count
        count = 0
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            if diff in prefix:
                count += prefix[diff]
            prefix[curSum] = 1 + prefix.get(curSum, 0)
        
        return count