class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap and hashMap[diff] != i:
                res.append(i)
                res.append(hashMap[diff])
                break
            
            hashMap[nums[i]] = i
        return sorted(res)