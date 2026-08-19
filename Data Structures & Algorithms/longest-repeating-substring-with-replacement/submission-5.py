class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # a hashmap should be useful for the frequency count
        # or a minheap works too
        # example 2 : AAABABB

        # if I were to traverse this string
        # I would ofcourse add that to the hashMap i = 2 : "A" : 3
        # i = 3 : "B" : 1
        # At this point, I have 3 As and 1 B, with k = 1
        # the only part I am not able to process is the actual way I can know about
        # whether the length is of the same characters
        # starting at l = 0 r = len(s) - 1 ??
        
        # Let me just get the frequencies in
        hashMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)

            while (r-l+1) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1
            
            res = max(res,(r-l+1))
        
        return res
        

            


