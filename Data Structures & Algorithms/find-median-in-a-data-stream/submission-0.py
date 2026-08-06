class MedianFinder:

    def __init__(self):
        #two heaps, large = minheap, small = maxheap
        #abs(len(small) - len(large)) <= 1
        self.small = [] #multiply by -1 for maxheap
        self.large = [] #this is default for Python (minheap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        #make sure every num in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        #check for uneven sizes
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large))%2 == 0:
            return (-1*self.small[0] + self.large[0])/2.0
        else:
            if len(self.small) > len(self.large):
                median = -1*self.small[0]
            else:
                median = self.large[0]
        return median
        