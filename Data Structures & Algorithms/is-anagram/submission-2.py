class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26

        for char in s:
            arr[ord(char) - 97] += 1

        for char in t:
            arr[ord(char) - 97] -= 1
        
        for count in arr:
            if count != 0:
                return False
        return True




 