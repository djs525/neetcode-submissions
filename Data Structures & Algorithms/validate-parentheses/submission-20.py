class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        hashMap = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for brac in s:
            if brac in hashMap:
                if stk:
                    bracket = stk.pop()
                    if hashMap[brac] == bracket:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stk.append(brac)
        
        return len(stk) == 0