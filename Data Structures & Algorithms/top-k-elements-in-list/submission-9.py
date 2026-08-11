class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []

        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i],0)

        while k > 0:
            maxKey = max(hashMap, key = hashMap.get)
            res.append(maxKey)
            hashMap[maxKey] = -1
            k -= 1
        return res
