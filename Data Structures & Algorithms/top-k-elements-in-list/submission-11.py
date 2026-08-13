class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        res = []
        # populating the hashMap
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        for i in range(k):
            max_key = max(hashMap, key=hashMap.get)
            res.append(max_key)
            hashMap[max_key] = -1
        
        return res
