class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        leftSum = 0
        rightSum = 0

        for p in range(1,len(nums)):
            prefix[p] = prefix[p-1] + nums[p]
        
        for pivot in range(len(nums)):
            if pivot == 0:
                leftSum = 0
            else:
                leftSum = prefix[pivot - 1]
            rightSum = prefix[len(nums) - 1] - prefix[pivot]
        
            if leftSum == rightSum:
                return pivot
        return -1
