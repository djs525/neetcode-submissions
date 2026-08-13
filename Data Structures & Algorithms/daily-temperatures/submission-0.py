class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stk = [] # store indices

        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stk and cur > temperatures[stk[-1]]:
                val = stk.pop()
                res[val] = i - val
            stk.append(i)
        return res