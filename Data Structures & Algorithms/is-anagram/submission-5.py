class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        for c in s:
            hashMap[c] = 1 + hashMap.get(c,0)
        
        for c in t:
            hashMap[c] = hashMap.get(c,0) - 1
        
        if all(x==0 for x in list(hashMap.values())):
            return True
        else:
            return False


 