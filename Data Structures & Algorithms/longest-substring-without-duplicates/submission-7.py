class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curLength = 0
        l = 0
        visited = set()

        for r in range(len(s)):
            while s[r] in visited:
                curLength -= 1
                visited.remove(s[l])
                l += 1
            
            curLength += 1
            visited.add(s[r])
            maxLength = max(maxLength, curLength)
        return maxLength