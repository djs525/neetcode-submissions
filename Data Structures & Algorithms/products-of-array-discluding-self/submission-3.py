class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)

        #for left prod
        for i in range(len(nums)):
            j = i + 1
            while j != len(nums):
                left_prod[i] *= nums[j]
                j += 1
        
        #for right prod
        for i in range(len(nums) - 1, -1 , -1):
            j = i-1
            while j != -1:
                right_prod[i] *= nums[j]
                j -= 1
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]
        return res
            
        

