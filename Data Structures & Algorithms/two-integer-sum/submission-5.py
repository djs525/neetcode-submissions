class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) - 1
        res = []

        hashMap = {}

        #populating the hashMap
        for i, n in enumerate(nums):
            hashMap[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashMap and hashMap[diff] != i:
                res.append(i)
                res.append(hashMap[diff])
                break
        return res
