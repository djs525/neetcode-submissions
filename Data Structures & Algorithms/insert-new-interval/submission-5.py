class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, curInterval in enumerate(intervals):

            # if newInterval starts after the curInterval ends
            if curInterval[1] < newInterval[0]:
                res.append(curInterval)
            
            # if newInterval ends before the curInterval starts
            elif newInterval[1] < curInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # now what if they overlap
            else:
                newInterval = [
                    min(curInterval[0],newInterval[0]),
                    max(curInterval[1], newInterval[1])]
        res.append(newInterval)
        return res