class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""
        
        # alright, we should have two hashMaps ofc
        # t has all the elements we need from s
        # we traverse s and try to match the elements count in t with s
        # once we find it, we can start reducing the substring until the match breaks
        # then we go back traversing the string s
        # we keep on updating the minWindow whenever we find a match
        # and also while we keep decreasing the substring until the match breaks

        # the only part is to understand how I can make the matches work here

        tCount = {}
        sCount = {}
        res = ""

        for i in range(len(t)):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        
        have = 0
        need = len(tCount)

        l = 0
        for r in range(len(s)):

            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
            
            while have==need:
                if not res:
                    res = s[l:r+1]
                
                if res and len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
            
                if sCount[s[l]] == 0:
                    del sCount[s[l]]
                l += 1
        return res
            
