class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1] * len(nums)
        rightProd = [1] * len(nums)

        for i in range(1,len(nums)):
            leftProd[i] = leftProd[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            rightProd[i] = rightProd[i+1] * nums[i+1]
        
        finalProd = [1] * len(nums)
        for i in range(len(nums)):
            finalProd[i] = leftProd[i] * rightProd[i]
        
        return finalProd