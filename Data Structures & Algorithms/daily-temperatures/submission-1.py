class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stk = [] # need to store indices

        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stk and i > 0 and cur > temperatures[stk[-1]]:
                idx = stk.pop()
                res[idx] = i - idx
            
            stk.append(i)
        return res