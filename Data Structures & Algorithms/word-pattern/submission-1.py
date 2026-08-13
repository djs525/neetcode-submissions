class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        wordsInStr = s.split()

        if len(pattern) != len(wordsInStr):
            return False
        
        hashMap = {} # {letter : word} and {word : letter}

        for i in range(len(pattern)):
            if (pattern[i] not in hashMap):
                hashMap[pattern[i]] = wordsInStr[i]

                if (wordsInStr[i] not in hashMap):
                    hashMap[wordsInStr[i]] = pattern[i]
                else:
                    return False
                
            else:
                if hashMap[pattern[i]] == wordsInStr[i]:
                    continue
                else:
                    return False
        return True

        
