class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {} # num : count

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        minHeap = []

        for n in hashMap.keys():
            heapq.heappush(minHeap, (hashMap[n], n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
            


