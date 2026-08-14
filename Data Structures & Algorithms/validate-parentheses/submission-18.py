class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # to store open brackets
        
        hashMap = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        for brac in s:
            if brac in hashMap:
                if stack:
                    bracket = stack.pop()
                    if hashMap[brac] == bracket:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(brac)
        return len(stack) == 0
