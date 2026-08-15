class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:

            #if array already sorted/ we are looking at the sorted portion
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res
            