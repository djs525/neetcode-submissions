class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        minHeap = []
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        for n in hashMap.keys():
            heapq.heappush(minHeap, (hashMap[n], n))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res