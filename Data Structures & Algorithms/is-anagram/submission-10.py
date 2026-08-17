class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #always think about the worst case scenario
        #eliminate that with guardrails like this one
        if len(s) != len(t):
            return False
        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1
        
        for c in t:
            arr[ord(c) - ord('a')] -= 1
        
        if min(arr) != 0:
            return False
        return True