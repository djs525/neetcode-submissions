class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = [0]
        res = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                idx = stk.pop()
                res[idx] = i - idx
            
            stk.append(i)
        return res