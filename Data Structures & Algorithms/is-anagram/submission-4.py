class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] * 26

        if len(s) != len(t):
            return False
        
        for char in s:
            array[ord(char) - ord('a')] += 1

        for char in t:
            array[ord(char) - ord('a')] -= 1

        for num in array:
            if num < 0 or num > 1:
                return False
        return True




 