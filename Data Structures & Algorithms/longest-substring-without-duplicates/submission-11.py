class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        exists = set()
        l = 0
        maxLength = 0
        curLength = 0

        for r in range(len(s)):
            while s[r] in exists:
                exists.remove(s[l])
                curLength -= 1
                l += 1
            exists.add(s[r])
            curLength += 1
            maxLength = max(maxLength, curLength)
        return maxLength