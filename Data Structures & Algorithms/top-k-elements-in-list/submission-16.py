class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #anytime we see top k
        #I would wanna use a heap data structure

        #i wanna use maxheap
        #the reason is i can pop the max element and append it
        #to a resulting array

        maxHeap = []

        #we'll need to save the frequency and the element as a tuple
        #in the heap
        #to store that we need a hashMap
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        res = []
        for n in hashMap.keys():
            heapq.heappush(maxHeap, (-1*hashMap[n], n))

        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res


        
