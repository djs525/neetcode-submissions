class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hashmap and i != hashmap[diff]:
                res.append(i)
                res.append(hashmap[diff])
                break
        return res
            



