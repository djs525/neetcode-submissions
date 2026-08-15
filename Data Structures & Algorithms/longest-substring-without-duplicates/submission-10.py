class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        l = 0

        curLength = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                curLength -= 1
                l += 1
            
            curLength += 1
            visited.add(s[r])
            maxLength = max(maxLength, curLength)
        
        return maxLength