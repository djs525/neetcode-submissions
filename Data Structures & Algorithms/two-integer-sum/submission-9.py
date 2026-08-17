class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #what could be the worst case here
        #if target cannot be reached, we can return []

        hashMap = {}

        for i, n in enumerate(nums):
            hashMap[n] = i
        
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap and hashMap[diff] != i:
                res.append(hashMap[diff])
                res.append(i)
                break
        
        return sorted(res)