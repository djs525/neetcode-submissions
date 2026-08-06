class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmap = {
            '}' : '{',
            ']' : '[',
            ')' : '('}
        if s == "":
            return True
        for i in range(len(s)):
            if s[i] in hashmap: #closing bracket
                if not stk or stk[-1] != hashmap[s[i]]:
                    return False
                stk.pop()

            else:
                stk.append(s[i])
        
        return len(stk) == 0