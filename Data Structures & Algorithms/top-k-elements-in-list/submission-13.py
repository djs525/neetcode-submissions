class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        res = []
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        for i in range(k):
            maxKey = max(hashMap, key = hashMap.get)
            res.append(maxKey)
            hashMap[maxKey] = -1
        return res
