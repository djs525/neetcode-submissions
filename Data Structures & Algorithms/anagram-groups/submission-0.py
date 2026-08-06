class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) 

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - 97] += 1
            hashmap[tuple(arr)].append(word)
        
        return list(hashmap.values())
            
        

                

                


        
