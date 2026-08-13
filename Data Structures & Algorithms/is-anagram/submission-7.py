class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        arr = [0] * 26

        if len(s) != len(t):
            return False
        
        #populating the arr with s
        for c in s:
            arr[ord(c) - ord('a')] += 1

        #depopulating the arr with t
        for c in t:
            arr[ord(c) - ord('a')] -= 1
        
        if min(arr) != 0:
            return False
        else:
            return True
        
