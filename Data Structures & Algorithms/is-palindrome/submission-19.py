class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #what's the worst possible scenario
        if s == "":
            return True
        
        #another thing is that it consists of lowercase and uppercase
        s = s.lower() # convert all to lowerCase

        l = 0
        r = len(s) - 1

        while l <= r:
            if not s[r].isalnum():
                r -= 1
                continue
            
            if not s[l].isalnum():
                l += 1
                continue
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True