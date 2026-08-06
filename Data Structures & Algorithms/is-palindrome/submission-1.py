class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        
        l,r = 0,len(s) - 1
        flag = 1
        while flag and l<=r:
            if s[l] != s[r]:
                flag = 0
                break
            l += 1
            r -= 1
        return bool(flag)
                