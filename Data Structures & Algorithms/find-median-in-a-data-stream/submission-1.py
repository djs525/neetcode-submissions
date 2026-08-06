class MedianFinder:

    def __init__(self):
        #small heap = max heap
        #large heap = min heap
        #python implements a heap as a minheap always
        #to work around it, we multiple each element
        #in the small heap by -1
        self.small = []
        self.large = []
    def addNum(self, num: int) -> None:
        #always add to the small heap and
        #then use pre-checks for the lengths to switch to large
        #all heap ops are O(logn)
        heapq.heappush(self.small, -1*num)

        #make sure every num in small <= every num in large
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = 1 * heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1*self.small[0] + self.large[0])/2
        
        