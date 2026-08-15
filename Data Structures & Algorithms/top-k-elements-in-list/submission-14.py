class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        minHeap = []
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        for n in hashMap.keys():
            heapq.heappush(minHeap, (hashMap[n], n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res

