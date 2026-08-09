class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square(num):
            ans = 0
            while num > 0:
                x = num % 10
                ans += x*x
                num = num // 10
            return ans

        slow = square(n)
        fast = square(square(n))

        while slow != fast:
            slow = square(slow)
            fast = square(square(fast))

            if slow == 1 or fast == 1:
                return True
        return slow == 1