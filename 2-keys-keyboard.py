class Solution:
    def minSteps(self, n: int) -> int:
        factors = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors += d
                n //= d
            d += 1
        
        if n > 1:
            factors += n
        
        return factors