class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        n = len(chars)
        i = 0
        while i < n:
            ch = chars[i] #a
            count = 0

            while i < n and chars[i] == ch:
                count += 1
                i += 1
            
            chars[idx] = ch
            idx += 1

            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        return idx
            