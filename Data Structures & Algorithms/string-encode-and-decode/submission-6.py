class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        
        return res
    
    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                j = i
                while s[j] != "#":
                    j += 1
                strLen = int(s[i:j])
                res.append(s[j+1:j+1+strLen])
            i = j + 1 + strLen
        return res




                    


