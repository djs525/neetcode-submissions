class Solution:
    def isValid(self, s: str) -> bool:
        
        # create a hashMap to store the different brackets

        hashMap = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        # initialize a stack
        stk = [] # we will store open brackets here


        for brac in s:
            #if brac is closed
            if brac in hashMap:
                # if stk exists
                if stk:
                    bracket = stk.pop()
                    # both open brackets should be the same for validity
                    # other words, open should be followed by closed
                    if hashMap[brac] == bracket:
                        continue
                    else:
                        return False
                # if stk doesn't exist, it means the string contains only closed bracket, invalid
                else:
                    return False
            
            # if the brac is open
            stk.append(brac)
        
        #at the end of the loop, stack has to be empty for a valid solution
        return len(stk) == 0
        