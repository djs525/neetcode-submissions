class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i,curInterval in enumerate(intervals):

            #newInterval ends before curInterval starts
            if newInterval[1] < curInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            #newInterval starts after curInterval ends
            elif newInterval[0] > curInterval[1]:
                res.append(curInterval)
            
            #they both overlap
            else:
                newInterval = [
                    min(newInterval[0], curInterval[0]),
                    max(newInterval[1], curInterval[1])
                ]
        res.append(newInterval)
        return res
        
