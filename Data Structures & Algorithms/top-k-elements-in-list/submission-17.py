class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Heap solution

        maxHeap = []
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        for n in hashMap.keys():
            heapq.heappush(maxHeap, (-1*hashMap[n], n))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res