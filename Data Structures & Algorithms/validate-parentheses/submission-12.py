class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for bracket in s:
            # for open brackets
            if bracket not in hashmap:
                stk.append(bracket)
                continue
            else:
                # s consists of only closed brackets hence not stk
                if not stk:
                    return False
                brac = stk.pop()
                #if the popped open not equal to the matching closed
                if brac != hashmap[bracket]:
                    return False
        
        return len(stk) == 0

                

                

            

                