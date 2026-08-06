class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            first = nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r:
                if -first == nums[l] + nums[r]:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                elif -first < nums[l] + nums[r]:
                    r -= 1
                
                else:
                    l += 1
        
        return res

                

