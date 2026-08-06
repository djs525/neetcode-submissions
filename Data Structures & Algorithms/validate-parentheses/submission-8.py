class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmap = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for bracket in s:
            if bracket not in hashmap:
                stk.append(bracket)
                continue
            else:
                if not stk:
                    return False
                brac = stk.pop()
                if brac != hashmap[bracket]:
                    return False
        
        return len(stk) == 0
            

                