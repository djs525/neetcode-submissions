class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hash = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for i in range(len(s)):
            if s[i] not in hash:
                stk.append(s[i])
            else:
                if not stk or hash[s[i]] != stk[-1]:
                    return False
                stk.pop()
        return len(stk) == 0