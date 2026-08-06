class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lcs = 0
        l = 0

        # lookup
        hashmap = {} #char->last seen index

        for r, ch in enumerate(s): # r acts as index, ch is the character
            if ch in hashmap and hashmap[ch] >= l:
                l = hashmap[ch] + 1
            hashmap[ch] = r #when if activates, then the key:value pair updates to the last seen index
            lcs = max(lcs, r-l+1)

        return lcs





