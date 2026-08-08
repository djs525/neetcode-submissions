class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = {0 : 1} #{sum : count}
        # ^ 0 always occurs atleast once with no elements

        curSum = 0
        count = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            if diff in prefixSum:
                count += prefixSum[diff]
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return count


        

