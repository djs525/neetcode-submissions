class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if not char.isalnum():
                continue
            new_s += char
        
        new_s = new_s.lower()

        l = 0
        r = len(new_s) - 1

        while l <= r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
        
                