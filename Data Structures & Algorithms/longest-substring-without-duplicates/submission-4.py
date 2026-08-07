class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curLength = 0
        l = 0
        duplicate = set()

        for r in range(len(s)):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                curLength -= 1
                l += 1
            
            duplicate.add(s[r])
            curLength += 1
            maxLength = max(maxLength, curLength)

        return maxLength