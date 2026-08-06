class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in s:
            if char not in hashmap:
                stk.append(char)
                continue
            else:
                if not stk:
                    return False
                brac = stk.pop()
                if brac != hashmap[char]:
                    return False
        
        return len(stk) == 0

                

            

                