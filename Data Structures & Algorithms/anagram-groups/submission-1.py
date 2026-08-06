class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            
            if tuple(arr) in hashmap:
                hashmap[tuple(arr)].append(word)
            else:
                hashmap[tuple(arr)] = [word]
            
        return list(hashmap.values())
        
        
            



                

                


        
