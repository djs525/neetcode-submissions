class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0

        l = 0
        r = 0
        charSet = set()
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            r += 1
            maxLength = max(maxLength, (r-l))
        
        return maxLength
