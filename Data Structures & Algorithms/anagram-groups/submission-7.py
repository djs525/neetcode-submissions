from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list) # {tuple(arr) : list of words}

        #populating the hashMap
        for s in strs:
            #initializing an arr for hashMap's key
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            hashMap[tuple(arr)].append(s)
        
        return list(hashMap.values())