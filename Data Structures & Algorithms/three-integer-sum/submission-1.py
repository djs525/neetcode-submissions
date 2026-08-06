class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            first = nums[i]
            if i > 0 and first == nums[i-1]:
                continue
            while l < r:
                if first + nums[l] + nums[r] == 0:
                    if [first,nums[l],nums[r]] not in res:
                        res.append([first,nums[l], nums[r]])
                    l+=1
                    r-=1
                elif first + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        return res

                

