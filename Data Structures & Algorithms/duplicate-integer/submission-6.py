class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        exists = set()

        for i in range(len(nums)):
            if nums[i] in exists:
                return True
            
            exists.add(nums[i])
        
        return False