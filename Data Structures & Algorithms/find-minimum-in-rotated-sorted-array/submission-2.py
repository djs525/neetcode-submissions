class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            mid = (l+r)//2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]: #mid is in the left sorted portion
                l = mid + 1 #search right
            else: #mid is in the right sorted portion
                r = mid #search left
        
        return res
            
            

        
