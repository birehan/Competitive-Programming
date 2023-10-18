class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(a, n):
            ans = 1
            while n > 0:
                if n & 1:
                    ans *= a

                a *= a
                n >>= 1
            
            return ans
            
        value = power(x, abs(n))
        if n < 0:
            value = 1/value
        
        return value


