class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i,n in enumerate(nums):
            hashMap[n] = i
        
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap and hashMap[diff] != i:
                res.append(hashMap[diff])
                res.append(i)
                break
        
        return sorted(res)