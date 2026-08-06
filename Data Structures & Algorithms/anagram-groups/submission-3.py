class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            freq_count = [0] * 26
            for char in string:
                freq_count[ord(char) - ord('a')] += 1
            
            hashmap[tuple(freq_count)].append(string)
        
        return list(hashmap.values())

        
        
            



                

                


        
