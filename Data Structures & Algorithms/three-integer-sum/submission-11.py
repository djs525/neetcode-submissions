class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        target = 0

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            diff = target - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[j] + nums[k] == diff:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > diff:
                    k -= 1
                else:
                    j += 1
        return res

