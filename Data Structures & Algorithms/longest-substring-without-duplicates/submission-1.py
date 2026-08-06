class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lcs = 0
        l = 0
        dupe = set()
        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1
            dupe.add(s[r])
            string_len = r-l+1
            lcs = max(lcs, string_len)

        return lcs


